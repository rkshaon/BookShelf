from django.urls import path
from rest_framework.routers import DefaultRouter

from book_api.views import v1


router = DefaultRouter()


router.register('genres', v1.GenreViewSet, basename='genre')
router.register('', v1.BookViewSet, basename='book')
router.register('topic', v1.TopicViewSet, basename='topics')

urlpatterns = [
    path(
        'update-cover-page/<int:book_code>/',
        v1.UpdateCoverPageFromBook.as_view()
    ),
]

urlpatterns += router.urls
