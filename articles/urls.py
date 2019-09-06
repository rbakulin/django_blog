from django.contrib import admin
from django.urls import path, re_path
from articles.views import ArticleView


urlpatterns = [
    path('', ArticleView.article_list, name='article_list'),
    path('<str:slug>', ArticleView.article_detail, name='article_detail'),
]
