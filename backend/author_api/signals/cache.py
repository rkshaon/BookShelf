from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver

from BookShelf.utilities.cache import invalidate_author_cache
from author_api.models import Author


@receiver(post_save, sender=Author)
def clear_author_cache_on_save(sender, instance, **kwargs):
    print('save\n\n')
    invalidate_author_cache()


@receiver(post_delete, sender=Author)
def clear_author_cache_on_delete(sender, instance, **kwargs):
    print('delete\n\n')
    invalidate_author_cache()
