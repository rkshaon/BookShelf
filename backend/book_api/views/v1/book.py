from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from BookShelf.utilities.pagination import Pagination
from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter
from activity_api.utilities.event import event_logger

from book_api.models import Book

from book_api.serializers.v1 import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(is_deleted=False)
    permission_classes = [
        IsAdminOrModerator,
    ]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    lookup_field = 'book_code'

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



# @method_decorator(cache_page(60*1), name='get')
# class BookView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         self.permission_classes = [IsAdminOrModerator]
#         self.check_permissions(request)
#         request.data['added_by'] = request.user.id
#         serializer = BookSerializer(
#             data=request.data,
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=201)
