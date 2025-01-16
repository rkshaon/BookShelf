from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

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
