from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from BookShelf.utilities.pagination import Pagination

from book_api.models import Genre

from book_api.serializers.v1 import GenreSerializer


class GenreView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk:
            try:
                genre = Genre.objects.get(
                    pk=pk, is_deleted=False
                )
            except Genre.DoesNotExist:
                raise NotFound(detail='Genre not found.')

            return Response(GenreSerializer(genre).data)

        genres = Genre.objects.filter(
            is_deleted=False
        ).order_by('-id')
        paginator = Pagination()
        page = paginator.paginate_queryset(genres, request)
        return paginator.get_paginated_response(
            GenreSerializer(page, many=True).data
        )
