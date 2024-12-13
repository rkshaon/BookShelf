from django.utils.deprecation import MiddlewareMixin

from django_user_agents.utils import get_user_agent

from BookShelf.utilities.client import get_client_ip
from BookShelf.utilities.client import get_device_type

from activity_api.models import Device


class DeviceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        device = self.get_log_device(
            request,
            request.user,
            get_client_ip(request)
        )

        request.device = device

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
        print(device, created)

        return device
