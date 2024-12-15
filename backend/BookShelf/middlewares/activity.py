from django.conf import settings

import json
import time

from activity_api.tasks import log_activity_async
from activity_api.tasks import update_activity_log


class ActivityLoggerMiddleware:
    """
    Middleware to log user activities.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        log_entry_id = self.log_request_start(request)
        response = self.get_response(request)
        self.log_response_end(request, log_entry_id)
        return response

    def log_request_start(self, request):
        if (
            request.path.startswith(settings.STATIC_URL) or
            request.path.startswith(settings.MEDIA_URL) or
            request.path.startswith('/admin/')
        ):
            return None
        device = getattr(request, 'device', None)
        activity_data = {
            'method': request.method,
            'path': request.path,
            'ip_address': getattr(request, 'ip_address', None),
            'device_id': device.id if device else None,
            'query_params': json.dumps(request.GET.dict()),
            'body': json.dumps(request.POST.dict() if request.POST else None),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
        }
        log_entry_id = log_activity_async.delay(activity_data).get()

        return log_entry_id

    def log_response_end(
        self,
        request,
        log_entry_id,
    ):
        if not log_entry_id:
            return

        duration = time.time() - request.start_time
        user = request.user if request.user.is_authenticated else None
        update_data = {
            'duration': duration,
            'user_id': user.id if user else None,
        }

        update_activity_log.delay(log_entry_id, update_data)
