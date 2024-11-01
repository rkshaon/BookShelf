from django.db.models.signals import post_delete
from django.dispatch import receiver

from book_api.models import Book


@receiver(post_delete, sender=Book)
def delete_book_files(sender, instance, *args, **kwargs):
    if instance.book:
        instance.book.delete(save=False)

    if instance.cover_image:
        instance.cover_image.delete(save=False)
