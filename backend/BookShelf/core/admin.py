# BookShelf/core/admin.py
from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        self._request = request
        return super().get_queryset(request)

    @property
    def user_timezone(self):
        request = getattr(self, '_request', None)
        if not request:
            return 'UTC'

        user_timezone = (
            request.user.timezone.name
            if hasattr(request.user, 'timezone') and request.user.timezone
            else 'UTC'
        )
        return user_timezone

    # def user_timezone_name(self):
    #     print('user_timezone_name')
    #     print(self.user_timezone)
    #     # return self.user_timezone
    #     return 'Local'
