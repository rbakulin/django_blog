from django.urls import path, include
from rest_framework import routers
from articles.views import ArticleView

router = routers.DefaultRouter()
router.register('articles', ArticleView)


urlpatterns = [
    path('', include(router.urls)),
]
