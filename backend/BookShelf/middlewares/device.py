from django.utils.deprecation import MiddlewareMixin
from django_user_agents.utils import get_user_agent

from BookShelf.utilities.client import get_device_type

from activity_api.models import Device


class DeviceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user if request.user.is_authenticated else None
        ip_address = request.ip_address
        device = self.get_log_device(
            request,
            user,
            ip_address
        )

        request.device = device

    def get_log_device(
        self,
        request,
        user,
        ip_address
    ):
        user_agent = get_user_agent(request)
        # device, created = Device.objects.get_or_create(
        #     user=user,
        #     user_agent=user_agent.ua_string,
        #     device_type=get_device_type(
        #         user_agent.is_mobile,
        #         user_agent.is_tablet,
        #         user_agent.is_pc
        #     ),
        #     browser=user_agent.browser.family,
        #     browser_version=user_agent.browser.version_string,
        #     os=user_agent.os.family,
        #     os_version=user_agent.os.version_string,
        #     ip_address=ip_address,
        #     screen_resolution=None,
        # )
        device = Device.objects.filter(
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
        ).first()

        if not device:
            device = Device.objects.create(
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

        return device
