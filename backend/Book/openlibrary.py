import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book, ReadingList
from django.db.utils import IntegrityError
from .models import ReadingList, UserDetails, ReadingListBook
from userauth.utils import IsUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Base URL for the Open Library API
OPEN_LIBRARY_SEARCH_URL = "https://openlibrary.org/search.json"
OPEN_LIBRARY_BOOK_URL = "https://openlibrary.org/works/"


@api_view(['GET'])
@permission_classes([IsUser])
def search_books(request):
    """Searches for books via Open Library based on a query."""
    query = request.GET.get('q', None)  # User search query

    if not query:
        return JsonResponse({"error": "Search query required"}, status=400)

    # Query Open Library API for the search term
    response = requests.get(OPEN_LIBRARY_SEARCH_URL, params={"q": query})
    data = response.json()

    # Process and return the first few books
    books = []
    for item in data.get("docs", [])[:10]:  # Limiting to 10 results for brevity
        books.append({
            "title": item.get("title"),
            "author_name": item.get("author_name", []),
            "cover_id": item.get("cover_i"),  # Cover image ID, if available
            "key": item.get("key")  # Key to retrieve full book details
        })

    return JsonResponse({"results": books})


def get_book_details(book_key):
    """Fetches full details of a book from Open Library."""
    response = requests.get(f"{OPEN_LIBRARY_BOOK_URL}{book_key}.json")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Book not found in Open Library")


@api_view(['POST'])  # Specify POST method
@permission_classes([IsUser])  # Ensure the user has necessary permissions
def add_book_to_account(request, book_key, user_id):
    """Adds a specific book to the user's account and database if not present."""
    user = get_object_or_404(UserDetails, pk=user_id)

    try:
        # Fetch book details from the external API
        book_data = get_book_details(book_key)

        # Retrieve or create the book in the database
        book, created = Book.objects.get_or_create(
            title=book_data.get("title"),
            author=book_data.get("authors", [{}])[0].get(
                "name", "Unknown Author"),
            genre=book_data.get("subjects", ["Unknown Genre"])[0],
            publication_year=int(book_data.get(
                "first_publish_date", "0").split("-")[0])
            if book_data.get("first_publish_date") else None,
            cover_image=f"https://covers.openlibrary.org/b/id/{book_data.get('covers', [])[0]}-L.jpg"
            if book_data.get("covers") else None,
        )

        # Add the book to the user's reading list
        reading_list, _ = ReadingList.objects.get_or_create(
            user=user, name="My Books")
        ReadingListBook.objects.create(
            reading_list=reading_list, book=book, status="Want to Read"
        )

        return JsonResponse({"message": f"Book '{book.title}' added to your account."})

    except IntegrityError:
        return JsonResponse({"error": "Book already in your account."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsUser])
def get_popular_books(request):
    """Fetches a list of popular books from Open Library for homepage display."""
    popular_books = []
    response = requests.get(f"{OPEN_LIBRARY_SEARCH_URL}?q=bestsellers")
    data = response.json()

    for item in data.get("docs", [])[:10]:  # Limiting to 10 popular books
        popular_books.append({
            "title": item.get("title"),
            "author_name": item.get("author_name", []),
            "cover_id": item.get("cover_i"),
            "key": item.get("key")
        })

    return JsonResponse({"popular_books": popular_books})
