from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from book_api.models import Genre


class GenreView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        genres = Genre.objects.filter(
            is_deleted=False
        )
        return Response()
