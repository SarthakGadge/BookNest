from django.urls import path
from .openlibrary import search_books, add_book_to_account, get_popular_books

urlpatterns = [
    path('search-books/', search_books, name='search_books'),
    path('add-book-to-account/<str:book_key>/<int:user_id>/',
         add_book_to_account, name='add_book_to_account'),
    path('popular-books/', get_popular_books, name='get_popular_books'),
]
