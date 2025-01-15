# from django.urls import path
from rest_framework.routers import DefaultRouter

from book_api.views import v1


router = DefaultRouter()

router.register('', v1.BookViewSet, basename='book')
router.register('genre', v1.GenreViewSet, basename='genre')
router.register('topic', v1.TopicViewSet, basename='topic')

urlpatterns = [
    # path('', v1.BookView.as_view()),
    # path('<int:book_code>/', v1.BookView.as_view()),
    # path('search', v1.BookSearchView.as_view()),
]

urlpatterns += router.urls
