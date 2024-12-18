from django.contrib import admin
from django.utils import timezone

import pytz

from activity_api.models import Device
from activity_api.models import ActivityLog
from activity_api.models import EventLog


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'os', 'browser', 'ip_address',
        'added_on_local',
    ]
    display_timezone = pytz.timezone('Asia/Dhaka')

    def added_on_local(self, obj):
        return timezone.localtime(
            obj.added_on,
            self.display_timezone
        ).strftime("%Y-%m-%d %I:%M:%S %p")

    added_on_local.short_description = 'Added On (Local)'

    list_per_page = 10
    list_display_links = (
        'user', 'os', 'browser', 'ip_address',
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
