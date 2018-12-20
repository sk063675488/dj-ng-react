from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
    )

from ..models import article_model
from .serializers import ArticleSerializer

class ArticleCreateView(CreateAPIView):
    queryset = article_model.objects.all()
    serializer_class = ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = article_model.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = article_model.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateView(UpdateAPIView):
    queryset = article_model.objects.all()
    serializer_class = ArticleSerializer

class ArticleDeleteView(DestroyAPIView):
    queryset = article_model.objects.all()
    serializer_class = ArticleSerializer