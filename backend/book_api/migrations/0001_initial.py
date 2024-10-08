# Generated by Django 5.1.1 on 2024-09-06 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author_api', '0003_author_died_date'),
        ('publisher_api', '0002_publisher_added_by_publisher_added_date_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='books')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers')),
                ('is_deleted', models.BooleanField(default=False)),
                ('added_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('authors', models.ManyToManyField(related_name='books', to='author_api.author')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='publisher_api.publisher')),
            ],
        ),
    ]
