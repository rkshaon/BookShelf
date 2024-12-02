
def get_client_ip(request):
    """Extract client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def get_device_type(
    is_mobile: bool,
    is_tablet: bool,
    is_pc: bool
) -> str:
    """Return device type based on user agent."""
    if is_mobile:
        return "mobile"
    if is_tablet:
        return "tablet"
    if is_pc:
        return "pc"
    # return "Unknown"
