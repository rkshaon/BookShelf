from django.urls import path

from user_api.views import v1


urlpatterns = [
    path(
        'registration',
        v1.UserRegistrationView.as_view(),
    ),
]
