from django.urls import path,re_path
from . import views

app_name='learning_logs'
urlpatterns = [
    # path('api/v1/article_list/',views.ArticleView.as_view(),name='art'),
    path('api/v1/artchapter/',views.ArtChapterView.as_view(),name='art_chapter'),
    path('api/v1/article/',views.ArticleView.as_view(),name='art_icle'),
    ]

