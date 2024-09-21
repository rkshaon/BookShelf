from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from BookShelf.utilities.pagination import Pagination

from book_api.models import Book

from book_api.serializers.v1 import BookSerializer


class BookView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        book_code = kwargs.get('book_code', None)
        genre = request.query_params.get('genre', None)
        topic = request.query_params.get('topic', None)

        if book_code:
            try:
                book = Book.objects.get(book_code=book_code, is_deleted=False)
            except Book.DoesNotExist:
                raise NotFound(detail="Book not found.")

            return Response(BookSerializer(book).data)

        books = Book.objects.filter(
            is_deleted=False
        )

        if genre:
            books = books.filter(genres__id=genre)

        if topic:
            books = books.filter(topics__id=topic)

        books = books.order_by('-id')
        paginator = Pagination()
        page = paginator.paginate_queryset(books, request)
        return paginator.get_paginated_response(
            BookSerializer(page, many=True).data
        )
