# Generated by Django 5.1.1 on 2024-11-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher_api', '0002_publisher_added_by_publisher_added_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
