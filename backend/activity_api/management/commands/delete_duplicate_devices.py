from django.core.management import BaseCommand

from django.db.models import Count, Min

from activity_api.models import Device


class Command(BaseCommand):
    help = "Delete duplicate Device entries."

    def handle(self, *args, **kwargs):
        duplicates = Device.objects.values(
            'user', 'device_type', 'browser', 'browser_version',
            'os', 'ip_address').annotate(
                min_id=Min('id'),
                count=Count('id')).filter(count__gt=1)
        keep_ids = [item['min_id'] for item in duplicates]

        for duplicate in duplicates:
            items = Device.objects.filter(
                user=duplicate['user'],
                device_type=duplicate['device_type'],
                browser=duplicate['browser'],
                browser_version=duplicate['browser_version'],
                os=duplicate['os'],
                ip_address=duplicate['ip_address'],
            ).exclude(id__in=keep_ids)
            items.delete()
            self.stdout.write(self.style.SUCCESS(f'\nDelete: {duplicate}'))
