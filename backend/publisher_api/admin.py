from django.contrib import admin

from publisher_api.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'address', 'website',
        'email', 'phone_number',
        'established_year',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = []
    search_fields = [
        'name', 'address', 'website',
        'email', 'phone_number',
        'established_year',
    ]
    readonly_fields = ['id',]
