from django.urls import path

from user_api.views import v1


urlpatterns = [
    path(
        'registration',
        v1.UserRegistrationView.as_view(),
    ),
    path(
        'login',
        v1.UserLoginView.as_view(),
    ),
    path(
        'profile',
        v1.UserProfileView.as_view(),
    ),
    path('refresh', v1.RefreshTokenView.as_view()),
]
