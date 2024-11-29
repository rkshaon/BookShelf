from django.urls import path
from rest_framework.routers import DefaultRouter

from book_api.views import v1


router = DefaultRouter()

router.register('genre', v1.GenreViewSet, basename='genre')

urlpatterns = [
    path('', v1.BookView.as_view()),
    path('<int:book_code>/', v1.BookView.as_view()),
    path('topic/', v1.TopicView.as_view()),
    path('topic/<int:pk>/', v1.TopicView.as_view()),
    path('search', v1.BookSearchView.as_view()),
]

urlpatterns += router.urls
