from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter

from book_api.models import Topic

from book_api.serializers.v1 import TopicSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.filter(is_deleted=False)
    serializer_class = TopicSerializer
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
            {"message": f"Topic '{instance.name}' has been successfully deleted."},   # noqa
            status=status.HTTP_200_OK,
        )
