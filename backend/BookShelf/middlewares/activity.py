from django.conf import settings

import json
import time

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
        ip_address = request.ip_address
        device = request.device
        self.log_response_end(
            request,
            log_entry,
            ip_address,
            device,
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
        device,
    ):
        if not log_entry:
            return

        duration = time.time() - request.start_time
        user = request.user if request.user.is_authenticated else None

        if user and not log_entry.user:
            log_entry.user = user

        log_entry.ip_address = ip_address
        log_entry.device = device
        log_entry.duration = duration
        log_entry.save()
