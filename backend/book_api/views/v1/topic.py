from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from book_api.models import Topic

from book_api.serializers.v1 import TopicSerializer

from BookShelf.utilities.pagination import Pagination


class TopicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if pk:
            try:
                topic = Topic.objects.get(
                    pk=pk, is_deleted=False
                )
            except Topic.DoesNotExist:
                raise NotFound(detail='Topic not found.')
        
            return Response(TopicSerializer(topic).data)
    
        topics = Topic.objects.filter(
            is_deleted=False
        ).order_by('-id')
        paginator = Pagination()
        page = paginator.paginate_queryset(topics, request)
        return paginator.get_paginated_response(
            TopicSerializer(page, many=True).data
        )
