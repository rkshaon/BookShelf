from django.contrib import admin

from activity_api.models import Device
from activity_api.models import ActivityLog
from activity_api.models import EventLog


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


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'device', 'activity_time',
    ]
    list_per_page = 10
    list_display_links = (
        'user', 'device',
    )
    search_fields = ()
    readonly_fields = (
        'id', 'duration', 'activity_time',
    )
    list_filter = []
    date_hierarchy = 'activity_time'


@admin.register(EventLog)
class EventLogAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'event', 'object', 'user', 'device', 'added_date_time',
    ]
    list_per_page = 10
    list_display_links = (
        'user', 'device',
    )
    search_fields = ()
    readonly_fields = (
        'id', 'added_date_time',
    )
    list_filter = []
    date_hierarchy = 'added_date_time'
