from django.contrib import admin

from configure_api.models import Timezone


@admin.register(Timezone)
class TimezoneAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
    ]
    list_per_page = 10
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    readonly_fields = (
        'id',
    )
