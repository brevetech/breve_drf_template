"this file is for the paginators class, of indexing pages"
from rest_framework.pagination import PageNumberPagination


class WithOutPagination(PageNumberPagination):
    """Page without pagination"""

    page_size = 10000
    page_size_query_param = "page_size"
    max_page_size = 10000


class DefaultPagination(PageNumberPagination):
    """Page with pagination"""

    page_size = 15
    page_size_query_param = "page_size"
    max_page_size = 10000
