from django.contrib import admin

from book_api.models import Genre
from book_api.models import Topic
from book_api.models import Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'slug',
    ]
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = ['id']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'slug',
    ]
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = ['id']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'book_code', 'title', 'cover', 'edition',
        'isbn', 'published_year', 'language',
        'is_deleted', 'uploader',
    ]
    list_per_page = 20

    @admin.display(boolean=True)
    def cover(self, obj):
        return bool(obj.cover)

    list_display_links = [
        'book_code', 'title',
    ]
    list_filter = [
        'genres',
    ]
    search_fields = [
        'title', 'edition', 'isbn',
        'published_year', 'language',
        'description',
    ]
    readonly_fields = ['id', 'book_code']
