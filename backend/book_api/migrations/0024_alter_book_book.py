# Generated by Django 5.1.1 on 2024-11-14 10:28

import BookShelf.utilities.storage
import BookShelf.utilities.validator
import book_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0023_alter_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(blank=True, max_length=255, null=True, storage=BookShelf.utilities.storage.ReplaceExistingFileStorage(), upload_to=book_api.models.book_upload_path, validators=[BookShelf.utilities.validator.validate_book_file_type]),
        ),
    ]
