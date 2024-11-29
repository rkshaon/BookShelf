# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import AllowAny
# from rest_framework.exceptions import NotFound

# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator

# from BookShelf.utilities.pagination import Pagination
from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter

from book_api.models import Genre

from book_api.serializers.v1 import GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.filter(is_deleted=False)
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

# @method_decorator(cache_page(60*15), name='get')
# class GenreView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if pk:
#             try:
#                 genre = Genre.objects.get(
#                     pk=pk, is_deleted=False
#                 )
#             except Genre.DoesNotExist:
#                 raise NotFound(detail='Genre not found.')

#             return Response(GenreSerializer(genre).data)

#         genres = Genre.objects.filter(
#             is_deleted=False
#         ).order_by('-id')
#         paginator = Pagination()
#         page = paginator.paginate_queryset(genres, request)
#         return paginator.get_paginated_response(
#             GenreSerializer(page, many=True).data
#         )
