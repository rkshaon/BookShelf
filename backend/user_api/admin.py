from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'role', 'is_active',
        'is_staff', 'is_superuser',
    )
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    readonly_fields = ('id',)
