from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'username', 'email', 'role', 'timezone',
        'is_active', 'is_staff', 'is_superuser', 'date_joined',
    )
    list_display_links = ['id', 'full_name', 'username', 'email']
    list_filter = ('role', 'is_active', 'is_staff')
    autocomplete_fields = ['timezone']
    search_fields = [
        'username', 'email', 'full_name'
    ]
    readonly_fields = (
        'id', 'added_date_time', 'updated_date_time',
    )

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)
