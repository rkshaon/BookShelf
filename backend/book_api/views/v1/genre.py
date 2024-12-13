from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter
from activity_api.utilities.event import event_logger

from book_api.models import Genre

from book_api.serializers.v1 import GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.filter(is_deleted=False).order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrModerator,
    ]
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Genre '{instance.name}' has been successfully deleted."},   # noqa
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        """Log the event when retrieving a single item."""
        response = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        event_logger(
            event='retrieve',
            object='genre',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
            data={
                'model': 'Genre',
                'id': instance.id
            }
        )

        return response

    def list(self, request, *args, **kwargs):
        """Log the event when retrieving a list of items."""
        response = super().list(request, *args, **kwargs)
        event_logger(
            event='retrieve',
            object='genre',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
        )

        return response
