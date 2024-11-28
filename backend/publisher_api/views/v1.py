from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from BookShelf.utilities.permissions import IsAdminOrReadOnly

from publisher_api.models import Publisher

from publisher_api.serializers import PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminOrReadOnly]
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
        # instance.deleted_by = self.request.user
        instance.is_deleted = True
        instance.save()

    # def get_queryset(self):
    #     return Publisher.objects.all().order_by('name')

    # def get_serializer_class(self):
    #     return PublisherSerializer

    # def get_permissions(self):
    #     return [IsAuthenticatedOrReadOnly()]

    # def get_authentication_classes(self):
    #     return [TokenAuthentication]
