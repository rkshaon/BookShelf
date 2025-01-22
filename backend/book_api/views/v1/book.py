from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
from django.conf import settings

from pdf2image import convert_from_path
from pathlib import Path

import os

from BookShelf.utilities.pagination import Pagination
from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter
from activity_api.utilities.event import event_logger

from book_api.models import Book

from book_api.serializers.v1 import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(
        is_deleted=False).order_by(
            '-id').distinct()
    permission_classes = [
        IsAdminOrModerator,
    ]
    filter_backends = [SearchFilter]
    pagination_class = Pagination
    search_fields = [
        'title', 'description',
        'authors__first_name',
        'authors__middle_name',
        'authors__last_name',
        'authors__biography',
        'genres__name',
        'genres__description',
        'topics__name',
        'publisher__name',
    ]
    lookup_field = 'book_code'

    def get_queryset(self):
        queryset = self.queryset
        genre = self.request.query_params.get('genre', None)
        topic = self.request.query_params.get('topic', None)

        filters = Q()
        if genre:
            filters &= Q(genres__id=genre)
        if topic:
            filters &= Q(topics__id=topic)

        return queryset.filter(filters)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": f"Book '{instance.title}' has been successfully deleted."    # noqa
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Log the event when retrieving a single item."""
        response = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        event_logger(
            event='retrieve',
            object='book',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
            data={
                'model': 'Book',
                'id': instance.id,
            }
        )

        return response

    def list(self, request, *args, **kwargs):
        """Log the event when retrieving a list of items."""
        response = super().list(request, *args, **kwargs)
        event_logger(
            event='retrieve',
            object='book',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
        )

        return response


class UpdateCoverPageFromBook(APIView):
    permission_classes = [
        IsAdminOrModerator,
    ]

    def patch(self, request, *args, **kwargs):
        book_code = kwargs.get('book_code', None)
        page_number = request.data.get('page_number', 1)

        try:
            book = Book.objects.get(book_code=book_code)
        except Book.DoesNotExist:
            return Response({
                'error': 'Book Not Found',
            }, status=status.HTTP_404_NOT_FOUND)

        if not book.book:
            return Response({
                'error': 'Book File Not Found.',
            }, status=status.HTTP_404_NOT_FOUND)

        book_path = book.book.path

        if book.pages < page_number:
            return Response({
                'error': 'Invalid page number.'
            }, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

        if not os.path.exists(book_path):
            return Response({
                "error": "Book is not available on the location."
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            images = convert_from_path(
                book_path,
                first_page=page_number,
                last_page=page_number,
                dpi=200
            )

            if not images:
                return Response({
                    "error": "Failed to extract page"
                }, status=status.HTTP_400_BAD_REQUEST)

            output_dir = Path(settings.MEDIA_ROOT) / "covers"
            output_dir.mkdir(parents=True, exist_ok=True)

            cover_image_path = output_dir / f"{book.book_code}.jpg"
            images[0].save(cover_image_path, format="JPEG")
            relative_cover_image_path = cover_image_path.relative_to(
                settings.MEDIA_ROOT)

            book.cover_image = str(relative_cover_image_path)
            book.save()

            return Response(
                BookSerializer(book).data,
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({
                "error": f"Failed to process the PDF: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
