from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from BookShelf.utilities.pagination import Pagination
from BookShelf.utilities.permissions import IsAdminOrModerator

from book_api.models import Book

from book_api.serializers.v1 import BookSerializer


@method_decorator(cache_page(60*1), name='get')
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

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminOrModerator]
        self.check_permissions(request)
        requested_data = request.data.copy()
        requested_data['added_by'] = request.user.id
        print(f"\nrequested_data: {requested_data}\n")
        serializer = BookSerializer(
            data=requested_data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
