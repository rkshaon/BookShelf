from activity_api.models import EventLog


def event_logger(
    event,
    object,
    user,
    device,
):
    EventLog.objects.create(
        event=event,
        object=object,
        user=user,
        device=device,
    )
    return None
