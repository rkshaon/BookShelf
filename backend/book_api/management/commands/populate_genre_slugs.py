from django.core.management.base import BaseCommand
from django.utils.text import slugify
from book_api.models import Genre


class Command(BaseCommand):
    help = 'Populate slugs for existing Genre records'

    def handle(self, *args, **kwargs):
        genres_without_slug = Genre.objects.filter(
            slug__isnull=True) | Genre.objects.filter(slug="")
        for genre in genres_without_slug:
            genre.slug = slugify(genre.name)
            genre.save()
            self.stdout.write(self.style.SUCCESS(
                f'Slug generated for Genre: {genre.name}'))
