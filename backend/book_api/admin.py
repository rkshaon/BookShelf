from django.contrib import admin

from book_api.models import Book


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
        'authors', 'publisher',
    ]
    search_fields = [
        'title', 'edition', 'isbn',
        'published_date', 'language',
        'description',
    ]
    readonly_fields = ['id',]
