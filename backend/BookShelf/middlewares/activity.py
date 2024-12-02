
from django.utils.timezone import now
from django.conf import settings

import json

from activity_api.models import ActivityLog


class ActivityLoggerMiddleware:
    """
    Middleware to log user activities.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request before the view is called
        response = self.get_response(request)

        # Log the request after the response is generated
        self.log_activity(request)

        return response

    def log_activity(self, request):
        # Skip logging for admin or static file requests
        if (
            request.path.startswith(settings.STATIC_URL) or
            request.path.startswith('/admin/')
        ):
            return

        # Capture user information
        user = request.user if request.user.is_authenticated else None

        # Capture request details
        activity_data = {
            'user': user,
            'method': request.method,
            'path': request.path,
            # Save query parameters
            'query_params': json.dumps(request.GET.dict()),
            # Save POST body
            'body': json.dumps(request.POST.dict() if request.POST else None),
            'timestamp': now(),
        }

        # Save the log to the database
        ActivityLog.objects.create(**activity_data)
