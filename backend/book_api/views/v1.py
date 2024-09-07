from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from BookShelf.utilities.pagination import Pagination

from book_api.models import Book

from book_api.serializers.v1 import BookSerializer


class BookView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(
            is_deleted=False
        )
        paginator = Pagination()
        page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
