from django.apps import AppConfig


class AuthorApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'author_api'

    def ready(self):
        # from author_api import signals  # noqa

        return super().ready()
