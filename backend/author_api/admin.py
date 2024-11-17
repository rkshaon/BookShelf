from django.contrib import admin
from django.contrib import messages

from author_api.models import Author


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
