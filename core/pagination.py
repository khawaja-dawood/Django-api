from rest_framework import pagination


# class MyCustomPagination(pagination.PageNumberPagination):
#     page_size = 5

class MyCustomPagination(pagination.LimitOffsetPagination):
    default_limit = 4
    max_limit = 15