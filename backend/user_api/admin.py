from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'username', 'email', 'role', 'is_active',
        'is_staff', 'is_superuser',
    )
    list_display_links = ['id', 'full_name', 'username', 'email']
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = [
        'username', 'email', 'full_name'
    ]
    readonly_fields = (
        'id', 'added_date_time', 'updated_date_time',
    )
