from functools import wraps
from activity_api.models import EventLog


def event_logger(event, object):
    """
    A decorator to log events such as retrieve, create, update, and delete.

    Args:
        action (str): The action performed (e.g., retrieve, create).
        object_type (str): The type of object (e.g., Book, Author).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Call the original function
            response = func(request, *args, **kwargs)
            user = request.user if hasattr(
                request, "user") and request.user.is_authenticated else None
            print(user)
            # print('Request:', request)
            # print('User:', request.user)
            print('Event:', event)
            print('Object:', object)
            print('Args:', args)
            print('Kwargs:', kwargs)

            # Extract object_id from kwargs if present
            # object_id = kwargs.get('pk') or kwargs.get('id')

            # Log the activity
            EventLog.objects.create(
                event=event,
                object=object,
                # object_id=object_id if object_id else 0,  # Use 0 if no specific object_id
                user=request.user if hasattr(request, 'user') else None
            )
            return response
        return wrapper
    return decorator
