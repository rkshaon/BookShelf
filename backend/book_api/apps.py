from django.apps import AppConfig


class BookApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_api'

    def ready(self) -> None:
        import book_api.signals # noqa
        return super().ready()
