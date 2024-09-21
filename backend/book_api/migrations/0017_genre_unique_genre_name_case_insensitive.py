# Generated by Django 5.1.1 on 2024-09-19 13:35

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0016_alter_genre_slug'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='unique_genre_name_case_insensitive'),
        ),
    ]