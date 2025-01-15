from django.db import models
from user_app.models import UserDetails


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    publication_year = models.PositiveIntegerField(
        null=True, blank=True)  # Optional: for numeric validation
    cover_image = models.URLField(null=True, blank=True)


class ReadingList(models.Model):
    user = models.ForeignKey(
        UserDetails, on_delete=models.CASCADE, related_name="reading_lists")
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures each user only has one reading list with the same name
        unique_together = ('user', 'name')


class ReadingListBook(models.Model):
    STATUS_CHOICES = [
        ("Want to Read", "Want to Read"),
        ("Currently Reading", "Currently Reading"),
        ("Read", "Read"),
    ]

    reading_list = models.ForeignKey(
        ReadingList, on_delete=models.CASCADE, related_name="books")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="in_lists")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Want to Read")

    class Meta:
        # Ensures no duplicate books in the same reading list
        unique_together = ("reading_list", "book")
