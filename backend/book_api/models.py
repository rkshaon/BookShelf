from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(
        'author_api.Author',
        related_name='books')
    publisher = models.ForeignKey(
        'publisher_api.Publisher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books')
    description = models.TextField(blank=True, null=True)
    edition = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    pdf_file = models.FileField(
        upload_to='books', blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='book_covers', blank=True, null=True)
    added_by = models.ForeignKey(
        'user_api.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
