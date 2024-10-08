# Generated by Django 5.1.1 on 2024-09-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_remove_user_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
