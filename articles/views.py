from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('date')
    serializer_class = ArticleSerializer

    @staticmethod
    def article_list(request):
        all_articles = ArticleView.queryset

        return render(request, "articles/article_list.html", {'all_articles': all_articles})

    @staticmethod
    def article_detail(request, slug):
        return HttpResponse(slug)
