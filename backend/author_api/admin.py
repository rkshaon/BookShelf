from django.contrib import admin
from django.contrib import messages

from author_api.models import Author
from book_api.models import Book


class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0
    verbose_name = "Book"
    verbose_name_plural = "Books"
    fields = ('book',)

    def book(self, obj):
        return obj.book.title
    book.short_description = "Book Title"


@admin.action(description='Mark as delete')
def delete_selected_authors(modeladmin, request, queryset):
    queryset.update(is_deleted=True)
    messages.success(request, 'Selected Authors have been deleted.')


# @admin.action(description='Permanent Delete all is_deleted Authors')
# def delete_all_is_deleted_authors(modeladmin, request, queryset):
#     # queryset.filter(is_deleted=True).delete()
#     # queryset.filter(is_deleted=True).delete()
#     authors = Author.objects.filter(is_deleted=True)
#     authors.delete()
#     messages.success(request, 'All is_deleted Authors have been deleted.')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'full_name', 'birth_date',
        'died_date', 'is_alive', 'is_deleted',
    ]
    list_per_page = 10
    list_display_links = ('id', 'full_name',)
    list_filter = [
        'is_deleted',
    ]
    search_fields = ('first_name', 'last_name', 'birth_date')
    readonly_fields = (
        'id', 'added_date_time', 'updated_date_time',
    )
    actions = [
        # delete_all_is_deleted_authors,
        delete_selected_authors,
    ]
    inlines = [
        BookInline,
    ]

    def get_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])
    get_books.short_description = "Books"

    list_display += ('get_books',)
