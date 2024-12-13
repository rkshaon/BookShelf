from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter
from activity_api.utilities.event import event_logger

from publisher_api.models import Publisher

from publisher_api.serializers import PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.filter(is_deleted=False)
    serializer_class = PublisherSerializer
    permission_classes = [
        IsAdminOrModerator,
    ]
    filter_backends = [SearchFilter]
    search_fields = ['name']
    # search_param = 'q'    # Default search query parameter is `search`
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        """
        Custom logic when creating a book instance.
        """
        serializer.save(added_by=self.request.user)

    def perform_update(self, serializer):
        """
        Custom logic when updating a book instance.
        """
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        """
        Custom logic when deleting a book instance.
        """
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        """
        Custom response after soft deleting an instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Publication '{instance.name}' has been successfully deleted."},   # noqa
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        event_logger(
            event='retrieve',
            object='publisher',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
            data={
                'model': 'Publisher',
                'id': instance.id
            }
        )
        return response

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        event_logger(
            event='retrieve',
            object='publisher',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
        )
        return response
    # def get_queryset(self):
    #     return Publisher.objects.all().order_by('name')

    # def get_serializer_class(self):
    #     return PublisherSerializer

    # def get_permissions(self):
    #     return [IsAuthenticatedOrReadOnly()]

    # def get_authentication_classes(self):
    #     return [TokenAuthentication]
