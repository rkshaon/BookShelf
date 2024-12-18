from django.contrib import admin
from django.utils.timezone import localtime

import pytz

from BookShelf.core.admin import BaseModelAdmin

from activity_api.models import Device
from activity_api.models import ActivityLog
from activity_api.models import EventLog


@admin.register(Device)
class DeviceAdmin(BaseModelAdmin):
    list_display = [
        'id', 'user', 'os', 'browser', 'ip_address',
        'added_on_local',
    ]

    def added_on_local(self, obj):
        try:
            display_timezone = pytz.timezone(self.user_timezone)
            return localtime(
                obj.added_on,
                display_timezone
            ).strftime("%d %B, %Y %I:%M:%S %p")
        except pytz.UnknownTimeZoneError:
            return localtime(obj.added_on).strftime("%Y-%m-%d %I:%M:%S %p")

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
class ActivityLogAdmin(BaseModelAdmin):
    list_display = [
        'id', 'user', 'device', 'activity_time_local',
    ]

    def activity_time_local(self, obj):
        try:
            display_timezone = pytz.timezone(self.user_timezone)
            return localtime(
                obj.activity_time,
                display_timezone
            ).strftime("%d %B, %Y %I:%M:%S %p")
        except pytz.UnknownTimeZoneError:
            return localtime(
                obj.activity_time
            ).strftime("%Y-%m-%d %I:%M:%S %p")

    activity_time_local.short_description = 'Activity Time (Local)'

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
class EventLogAdmin(BaseModelAdmin):
    list_display = [
        'id', 'event', 'object', 'user', 'device', 'added_date_time_local',
    ]

    def added_date_time_local(self, obj):
        try:
            display_timezone = pytz.timezone(self.user_timezone)
            return localtime(
                obj.added_date_time,
                display_timezone
            ).strftime("%d %B, %Y %I:%M:%S %p")
        except pytz.UnknownTimeZoneError:
            return localtime(
                obj.added_date_time
            ).strftime("%Y-%m-%d %I:%M:%S %p")

    added_date_time_local.short_description = 'Added Date Time (Local)'

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
