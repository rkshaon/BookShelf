from django.db import models
from django.utils.timezone import now

import os
import uuid


def book_upload_path(instance, filename):
    """
    Generates a unique file path and renames the file with a unique code.
    """
    ext = filename.split('.')[-1]
    current_time = now().strftime('%Y%m%d%H%M%S%f')
    unique_code = str(uuid.uuid4().int)[:10]
    new_filename = f'{unique_code}{current_time}.{ext}'

    return os.path.join('books', new_filename)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(
        'book_api.Genre',
        related_name='books'
    )
    topics = models.ManyToManyField(
        'book_api.Topic',
        related_name='books'
    )
    authors = models.ManyToManyField(
        'author_api.Author',
        related_name='books')
    publisher = models.ForeignKey(
        'publisher_api.Publisher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books')
    description = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    book = models.FileField(
        upload_to=book_upload_path, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='book_covers', blank=True, null=True)
    added_by = models.ForeignKey(
        'user_api.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
