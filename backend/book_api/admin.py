from django.contrib import admin
from django.utils.html import format_html

from BookShelf.settings import FRONTEND_BASE_URL

from book_api.models import Genre
from book_api.models import Topic
from book_api.models import Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'slug', 'is_deleted',
    ]
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = [
        'id', 'added_date_time', 'updated_date_time',
    ]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'slug', 'is_deleted',
    ]
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = [
        'id', 'added_date_time', 'updated_date_time',
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'book_code', 'title', 'cover', 'edition',
        'pages', 'isbn', 'published_year', 'language',
        'is_deleted', 'uploader', 'open_url',
    ]
    list_per_page = 10

    @admin.display(boolean=True)
    def cover(self, obj):
        return bool(obj.cover)

    def open_url(self, obj):
        return format_html(
            '<a href="{}" target="_blank">Click</a>',
            f"{FRONTEND_BASE_URL}/book/{obj.book_code}"
        )
    open_url.short_description = 'Read'

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
    readonly_fields = [
        'id', 'book_code', 'added_date_time', 'updated_date_time',
    ]
