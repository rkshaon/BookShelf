from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from BookShelf.utilities.pagination import Pagination
from book_api.documents import BookDocument
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     SearchFilterBackend,
# )


class BookSearchView(APIView):
    permission_classes = [AllowAny]
    pagination_class = Pagination

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', None)

        if not query:
            return Response({
                "error": "No search query provided."
            }, status=status.HTTP_400_BAD_REQUEST)

        # search_results = BookDocument.search().query(
        #     "multi_match",
        #     query=query,
        #     fields=[
        #         "title",
        #         "authors.name",
        #         "genres.name",
        #         "topics.name"
        #     ],
        #     fuzziness="AUTO",
        # )
        # old code
        # search_results = BookDocument.search().query(
        #     "bool",
        #     should=[{
        #         "multi_match": {
        #             "query": query,
        #             "fields": [
        #                 "title",
        #                 "authors.name",
        #                 "genres.name",
        #                 "topics.name"],
        #             "fuzziness": "AUTO"
        #         }},
        #         {
        #             "wildcard": {
        #                 "title": f"*{query.lower()}*"
        #             }
        #         },
        #         {
        #             "wildcard": {
        #                 "authors.name": f"*{query.lower()}*"
        #             }
        #         },
        #         {
        #             "wildcard": {
        #                 "genres.name": f"*{query.lower()}*"
        #             }
        #         },
        #         {
        #             "wildcard": {
        #                 "topics.name": f"*{query.lower()}*"
        #             }
        #         }
        #     ],
        #     minimum_should_match=1
        # )

        # # results = [hit.to_dict() for hit in search_results]
        # paginator = self.pagination_class()
        # paginated_results = paginator.paginate_queryset(
        #     search_results, request)
        # print(paginated_results)
        # return paginator.get_paginated_response(paginated_results)

        # # return Response(results, status=status.HTTP_200_OK)
        # Convert the search results to a list of dictionaries
        # Use multi_match with the correct field names
        search_results = BookDocument.search().query(
            "multi_match",
            query=query,
            fields=[
                "title",
                "authors.full_name",  # Correct field name
                "genres.name",
                "topics.name"
            ],
            fuzziness="AUTO"
        )
        results = [hit.to_dict() for hit in search_results]
        print(search_results.to_dict())

        # Paginate the results
        paginator = self.pagination_class()
        paginated_results = paginator.paginate_queryset(results, request)

        # Return the paginated results as a JSON response
        return paginator.get_paginated_response(paginated_results)
