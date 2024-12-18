from django.db import models

import pytz


class Timezone(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def populate_timezones():
        """Populates the Timezone table with all pytz timezones."""
        for tz in pytz.all_timezones:
            Timezone.objects.get_or_create(name=tz)
