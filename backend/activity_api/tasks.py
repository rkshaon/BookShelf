from celery import shared_task

import logging

from activity_api.models import ActivityLog

logger = logging.getLogger(__name__)


@shared_task
def log_activity_async(activity_data):
    """
    Asynchronous task to log activity data.
    """
    log_entry = ActivityLog.objects.create(**activity_data)
    return log_entry.id


@shared_task
def update_activity_log(log_entry_id, update_data):
    """
    Asynchronous task to update an existing ActivityLog entry.
    """
    try:
        log_entry = ActivityLog.objects.get(id=log_entry_id)
        for key, value in update_data.items():
            setattr(log_entry, key, value)
        log_entry.save()
        return f"Log entry {log_entry_id} updated successfully."
    except ActivityLog.DoesNotExist:
        return f"Log entry {log_entry_id} not found."
    except Exception as e:
        return f"Error updating log entry {log_entry_id}: {str(e)}"
