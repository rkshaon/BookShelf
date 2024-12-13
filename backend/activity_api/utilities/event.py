from activity_api.models import EventLog


def event_logger(
    event,
    object,
    user,
    device,
    ip_address,
    data
) -> None:
    if user.is_anonymous:
        user = None

    EventLog.objects.create(
        event=event,
        object=object,
        user=user,
        device=device,
        ip_address=ip_address,
        data=data,
    )
    return None
