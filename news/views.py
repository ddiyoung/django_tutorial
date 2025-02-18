from django.shortcuts import render

from .models import Article, Reporter

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .pagination import ArticlePagination
from .serializers import ArticleSerializer, ReporterSerializer
from rest_framework import generics

# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

class ArticleDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    queryset =  Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

class ArticleListView(generics.ListAPIView):

    authentication_classes = []
    permission_classes = []

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    lookup_field = 'id'

class ArticleCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


