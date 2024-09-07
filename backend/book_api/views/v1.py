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
        pk = kwargs.get('pk', None)

        if pk:
            try:
                book = Book.objects.get(pk=pk, is_deleted=False)
            except Book.DoesNotExist:
                raise NotFound(detail="Book not found.")

            return Response(BookSerializer(book).data)

        books = Book.objects.filter(
            is_deleted=False
        ).order_by('id')
        paginator = Pagination()
        page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
