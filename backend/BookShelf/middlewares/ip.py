from BookShelf.utilities.client import get_client_ip


class IPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = get_client_ip(request)
        request.ip_address = ip_address
        response = self.get_response(request)

        return response
