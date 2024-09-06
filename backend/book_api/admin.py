from django.contrib import admin

from book_api.models import Genre
from book_api.models import Topic
from book_api.models import Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
    ]
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = ['id']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'edition', 'isbn',
        'published_date', 'language',
        'is_deleted',
    ]
    list_display_links = [
        'title',
    ]
    list_filter = [
        'genres', 'authors', 'publisher',
    ]
    search_fields = [
        'title', 'edition', 'isbn',
        'published_date', 'language',
        'description',
    ]
    readonly_fields = ['id',]
