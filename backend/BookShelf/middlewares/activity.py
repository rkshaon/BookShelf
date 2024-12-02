# from django.utils.timezone import now
from django.conf import settings
from django_user_agents.utils import get_user_agent

import json
import time

from BookShelf.utilities.client import get_client_ip
from BookShelf.utilities.client import get_device_type

from activity_api.models import Device
from activity_api.models import ActivityLog


class ActivityLoggerMiddleware:
    """
    Middleware to log user activities.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        log_entry = self.log_request_start(request)
        response = self.get_response(request)
        ip_address = get_client_ip(request)
        self.log_response_end(
            request,
            log_entry,
            ip_address
        )

        return response

    def log_request_start(self, request):
        if (
            request.path.startswith(settings.STATIC_URL) or
            request.path.startswith(settings.MEDIA_URL) or
            request.path.startswith('/admin/')
        ):
            return

        activity_data = {
            'method': request.method,
            'path': request.path,
            'query_params': json.dumps(request.GET.dict()),
            'body': json.dumps(request.POST.dict() if request.POST else None),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
        }

        log_entry = ActivityLog.objects.create(**activity_data)

        return log_entry

    def log_response_end(
        self,
        request,
        log_entry,
        ip_address,
    ):
        if not log_entry:
            return

        duration = time.time() - request.start_time
        user = request.user if request.user.is_authenticated else None

        if user and not log_entry.user:
            log_entry.user = user

        log_entry.ip_address = ip_address
        log_entry.device = self.get_log_device(
            request,
            user,
            ip_address,
        )
        log_entry.duration = duration
        log_entry.save()

    def get_log_device(
        self,
        request,
        user,
        ip_address
    ):
        user_agent = get_user_agent(request)
        device, created = Device.objects.get_or_create(
            user=user,
            user_agent=user_agent.ua_string,
            device_type=get_device_type(
                user_agent.is_mobile,
                user_agent.is_tablet,
                user_agent.is_pc
            ),
            browser=user_agent.browser.family,
            browser_version=user_agent.browser.version_string,
            os=user_agent.os.family,
            os_version=user_agent.os.version_string,
            ip_address=ip_address,
            screen_resolution=None,
        )

        return device
