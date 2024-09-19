from django.urls import path

from book_api.views import v1


urlpatterns = [
    path('', v1.BookView.as_view()),
    path('<int:book_code>/', v1.BookView.as_view()),
    path('genre/', v1.GenreView.as_view()),
    path('genre/<int:pk>/', v1.GenreView.as_view()),
]
