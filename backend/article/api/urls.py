from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView
    )

urlpatterns =[
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view())
]