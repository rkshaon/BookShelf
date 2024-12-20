from django.contrib import admin

from BookShelf.core.admin import BaseModelAdmin

from publisher_api.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(BaseModelAdmin):
    list_display = [
        'id', 'name', 'address', 'website',
        'email', 'phone_number', 'established_year',
        'is_deleted', 'added_by',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = []
    search_fields = [
        'name', 'address', 'website', 'email',
        'phone_number', 'established_year',
    ]
    readonly_fields = [
        'id', 'added_date_time', 'updated_date_time',
    ]
