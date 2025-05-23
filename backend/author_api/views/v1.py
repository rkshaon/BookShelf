from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Q

from BookShelf.utilities.pagination import Pagination
from BookShelf.utilities.permissions import IsAdminOrModerator
from BookShelf.utilities.filters import SearchFilter
from activity_api.utilities.event import event_logger

from author_api.models import Author

from author_api.serializers.v1 import AuthorSerializer


@method_decorator(cache_page(60*1), name='get')
class AuthorView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = [
        'first_name', 'middle_name', 'last_name',
        'biography',
    ]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        query = request.query_params.get('search', None)

        if pk:
            try:
                author = Author.objects.get(pk=pk, is_deleted=False)
            except Author.DoesNotExist:
                raise NotFound(detail='Author not found.')

            event_logger(
                event='retrieve',
                object='author',
                user=request.user,
                device=request.device,
                ip_address=request.ip_address,
                data={
                    'model': 'Author',
                    'id': author.id
                }
            )

            return Response(
                AuthorSerializer(
                    author, context={'include_books': True}
                ).data)

        authors = Author.objects.filter(
            is_deleted=False
        ).order_by('-id')

        # if query:
        #     search_query = Q()
        #     for field in self.search_fields:
        #         search_query |= Q(**{f"{field}__icontains": query})
        #     authors = authors.filter(search_query)
        if query:
            search_query = Q()
            search_terms = query.split()
            for term in search_terms:
                term_query = Q()
                for field in self.search_fields:
                    term_query |= Q(**{f"{field}__icontains": term})
                search_query &= term_query
            authors = authors.filter(search_query)

        paginator = Pagination()
        page = paginator.paginate_queryset(authors, request)
        serializer = AuthorSerializer(page, many=True)

        event_logger(
            event='retrieve',
            object='author',
            user=request.user,
            device=request.device,
            ip_address=request.ip_address,
        )

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsAdminOrModerator]
        self.check_permissions(request)
        request.data['added_by'] = request.user.id
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
