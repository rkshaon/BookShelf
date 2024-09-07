# BookShelf/utilities/pagination
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_page_size(self, request):
        """
        Handle dynamic page_size via query parameter
        or fall back to default.
        """
        if request.query_params.get(self.page_size_query_param):
            return min(
                int(request.query_params[self.page_size_query_param]),
                self.max_page_size
            )
        return self.page_size
