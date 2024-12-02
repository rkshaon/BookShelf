from django.contrib import admin

from activity_api.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'os', 'browser', 'ip_address', 'added_on',
    ]
    list_per_page = 10
    list_display_links = (
        'user', 'os', 'browser', 'ip_address', 'added_on',
    )
    search_fields = ('os', 'browser', 'ip_address')
    readonly_fields = (
        'id', 'added_on',
    )
    list_filter = [
        'os', 'browser',
    ]
    date_hierarchy = 'added_on'
