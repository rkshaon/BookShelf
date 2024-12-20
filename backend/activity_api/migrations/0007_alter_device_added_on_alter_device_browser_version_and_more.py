# Generated by Django 5.1.1 on 2024-12-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_api', '0006_eventlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added On'),
        ),
        migrations.AlterField(
            model_name='device',
            name='browser_version',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Browser Version'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(blank=True, choices=[('mobile', 'Mobile'), ('tablet', 'Tablet'), ('pc', 'PC')], max_length=10, null=True, verbose_name='Device Type'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='device',
            name='os_version',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='OS Version'),
        ),
        migrations.AlterField(
            model_name='device',
            name='screen_resolution',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Screen Resolution'),
        ),
        migrations.AlterField(
            model_name='device',
            name='user_agent',
            field=models.JSONField(blank=True, null=True, verbose_name='User Agent'),
        ),
    ]
