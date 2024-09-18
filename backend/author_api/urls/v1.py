from django.urls import path

from author_api.views import v1


urlpatterns = [
    path('', v1.AuthorView.as_view()),
    path('<int:pk>/', v1.AuthorView.as_view()),
]
