from django.apps import AppConfig


class UserApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_api'
    verbose_name = 'User'

    def ready(self):
        import user_api.signals # noqa
        return super().ready()
