from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from BookShelf.utilities.pagination import Pagination

from author_api.models import Author

from author_api.serializers.v1 import AuthorSerializer


class AuthorView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk:
            try:
                author = Author.objects.get(pk=pk, is_deleted=False)
            except Author.DoesNotExist:
                raise NotFound(detail='Author not found.')

            return Response(AuthorSerializer(author).data)

        authors = Author.objects.filter(
            is_deleted=False
        ).order_by('-id')
        paginator = Pagination()
        page = paginator.paginate_queryset(authors, request)
        serializer = AuthorSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
