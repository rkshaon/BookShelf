# Generated by Django 5.1.1 on 2024-12-18 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configure_api', '0001_initial'),
        ('user_api', '0005_rename_cover_image_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='timezone',
            field=models.ForeignKey(blank=True, default=None, help_text="User's preferred timezone", null=True, on_delete=django.db.models.deletion.SET_NULL, to='configure_api.timezone'),
        ),
    ]