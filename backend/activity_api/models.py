from django.db import models
from django.utils.translation import gettext_lazy as _

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


class ActivityLog(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    device = models.ForeignKey(
        Device,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    method = models.CharField(max_length=10)
    path = models.TextField()
    query_params = models.TextField(
        _('Query Params'),
        null=True,
        blank=True
    )
    body = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(
        _('User Agent'),
        null=True,
        blank=True
    )
    ip_address = models.GenericIPAddressField(
        _('IP Address'),
        null=True,
        blank=True
    )
    duration = models.FloatField(null=True, blank=True)
    activity_time = models.DateTimeField(
        _('Activity Time'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Activity Log')
        verbose_name_plural = _('Activity Logs')

    def __str__(self):
        user_info = f"User: {self.user}" if self.user else "Anonymous"
        return f"{user_info} - {self.method} - {self.path} - {self.timestamp}"
