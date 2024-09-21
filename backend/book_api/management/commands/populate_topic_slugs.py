from django.core.management.base import BaseCommand
from django.utils.text import slugify
from book_api.models import Topic


class Command(BaseCommand):
    help = 'Populate slugs for existing Topic records'

    def handle(self, *args, **kwargs):
        topics_without_slug = Topic.objects.filter(
            slug__isnull=True) | Topic.objects.filter(slug="")
        for topic in topics_without_slug:
            topic.slug = slugify(topic.name)
            topic.save()
            self.stdout.write(self.style.SUCCESS(
                f'Slug generated for Topic: {topic.name}'))
