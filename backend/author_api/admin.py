from django.contrib import admin

from author_api.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'full_name', 'birth_date',
        'died_date', 'is_alive',
    ]
    list_display_links = ('id', 'full_name',)
    # list_filter = ('is_alive',)
    search_fields = ('first_name', 'last_name', 'birth_date')
    readonly_fields = ('id',)
