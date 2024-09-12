from django.db import models
from django.utils.timezone import now

import os
import uuid

from BookShelf.utilities.storage import ReplaceExistingFileStorage


replace_existing_file_storage = ReplaceExistingFileStorage()


def book_upload_path(instance, filename):
    """
    Generates a unique file path
    and renames the file with the book code.
    """
    ext = filename.split('.')[-1]
    new_filename = f"{instance.book_code}.{ext}"

    return os.path.join('books', new_filename)


def cover_upload_path(instance, filename):
    """
    Generates a unique file path
    and renames the file with the book code.
    """
    ext = filename.split('.')[-1]
    new_filename = f"{instance.book_code}.{ext}"

    return os.path.join('covers', new_filename)


def generate_book_code():
    """
    Generates a unique book code.
    """
    current_time = now().strftime('%Y%m%d%H%M%S%f')
    book_code = str(uuid.uuid4().int)[:10]
    book_code = int(f'{book_code}{current_time}')

    return book_code


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    book_code = models.CharField(
        max_length=255,
        default=generate_book_code,
        unique=True,
        editable=False
    )
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(
        'book_api.Genre',
        related_name='books',
        blank=True,
    )
    topics = models.ManyToManyField(
        'book_api.Topic',
        related_name='books',
        blank=True,
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
    isbn = models.CharField(max_length=20, blank=True, null=True, unique=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    book = models.FileField(
        upload_to=book_upload_path,
        max_length=255,
        blank=True,
        null=True,
        storage=replace_existing_file_storage
    )
    cover_image = models.ImageField(
        upload_to=cover_upload_path,
        blank=True,
        null=True,
        storage=replace_existing_file_storage
    )
    added_by = models.ForeignKey(
        'user_api.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    @property
    def cover(self) -> bool:
        return bool(self.cover_image)

    @property
    def uploader(self):
        return self.added_by

    def __str__(self):
        authors = ", ".join([
            author.full_name for author in self.authors.all()
        ])
        return f"{self.title} by {authors}"
