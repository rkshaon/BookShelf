from django.contrib import admin

from book_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'edition', 'isbn',
        'is_deleted',
    ]
