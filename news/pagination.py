from rest_framework.pagination import PageNumberPagination

class ArticlePagination(PageNumberPagination):
    page_size = 3  # 🔹 한 페이지당 3개
    page_size_query_param = 'page_size'  # 🔹 URL에서 개수 조절 가능 (예: ?page_size=20)
