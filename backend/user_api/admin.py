from django.contrib import admin
from django.utils.timezone import localtime

import pytz

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'username', 'email', 'role', 'timezone',
        'is_active', 'is_staff', 'is_superuser', 'date_joined_local',
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

    @property
    def user_timezone(self):
        request = self._request
        user_timezone = request.user.timezone.name if hasattr(
            request.user, 'timezone') and request.user.timezone else 'UTC'
        return user_timezone

    def date_joined_local(self, obj):
        """
            Convert date_joined to the logged-in user's preferred
            timezone.
        """
        try:
            display_timezone = pytz.timezone(self.user_timezone)
            return localtime(
                obj.date_joined,
                display_timezone
            ).strftime("%d %B, %Y %I:%M:%S %p")
        except pytz.UnknownTimeZoneError:
            return localtime(obj.date_joined).strftime("%Y-%m-%d %I:%M:%S %p")

    date_joined_local.short_description = "Date Joined (Local)"

    def get_queryset(self, request):
        """
            Attach the request object to the admin instance
            for access in custom methods.
        """
        self._request = request
        return super().get_queryset(request)

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)
