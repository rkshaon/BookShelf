from django.db import models
# from django.contrib.postgres.fields import JSONField

from user_api.models import User

from BookShelf.global_variables import DEVICE_TYPE


class Device(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user_agent = models.JSONField(
        blank=True,
        null=True
    )
    device_type = models.CharField(
        max_length=10,
        choices=DEVICE_TYPE,
        blank=True,
        null=True
    )
    browser = models.CharField(max_length=50, blank=True, null=True)
    browser_version = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    os = models.CharField(max_length=50, blank=True, null=True)
    os_version = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )
    screen_resolution = models.CharField(max_length=20, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_info = f"User: {self.user}" if self.user else "Anonymous"
        return f"{user_info} - {self.os} - {self.browser} ({self.ip_address})"

# class ActivityLog(models.Model):
#     user = models.ForeignKey(
#         User, null=True, blank=True, on_delete=models.SET_NULL)
#     method = models.CharField(max_length=10)
#     path = models.TextField()
#     query_params = models.TextField(null=True, blank=True)
#     body = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     user_agent = models.TextField(null=True, blank=True)
#     ip_address = models.GenericIPAddressField(
#         null=True, blank=True)
#     duration = models.FloatField(null=True, blank=True)
