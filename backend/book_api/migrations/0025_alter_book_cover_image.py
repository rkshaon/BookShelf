# Generated by Django 5.1.1 on 2025-01-22 19:18

import BookShelf.utilities.storage
import book_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0024_alter_book_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=255, null=True, storage=BookShelf.utilities.storage.ReplaceExistingFileStorage(), upload_to=book_api.models.cover_upload_path),
        ),
    ]
