from django.db.models.signals import post_save
from django.dispatch import receiver

from PyPDF2 import PdfReader

from book_api.models import Book


@receiver(post_save, sender=Book)
def update_book_page_count(sender, instance, created, **kwargs):
    if instance.book and not instance.pages:
        try:
            book_path = instance.book.path
            reader = PdfReader(book_path)
            instance.pages = len(reader.pages)
            instance.save()
        except Exception as e:
            print(f"\nError calculating page count: {e}\n")
