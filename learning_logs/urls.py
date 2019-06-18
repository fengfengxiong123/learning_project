"""learning_logs URL Configuration
"""

from django.urls import path, include,re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'article_list', views.ArticleViewSet)
app_name='learning_logs'
urlpatterns = [    
    # path('',views.index,name='index'),
    # re_path(r'^article/(?P<article_id>\d+)/$', views.article,name='article'),
    # re_path(r'^look_chapter/(?P<chapter_id>\d+)/$', views.look_chapter,name='look_chapter'),
    # re_path(r'^new_chapter/(?P<article_id>\d+)/$', views.new_chapter,name='new_chapter'),
    #
    # # re_path(r'^edit_chapter/(?P<article_id>\d+)(?P<chapter_id>\d+)/$', views.edit_chapter,name='edit_chapter'),
    # re_path(r'^edit_chapter/(\d+)/(\w+)/$',views.edit_chapter,name='edit_chapter'),
    #
    # re_path(r'^edit_art_chapter/(?P<article_id>\d+)/$', views.edit_art_chapter,name='edit_art_chapter'),
    # re_path(r'^new_article/$', views.new_article, name='new_article'),
    # re_path(r'^search/$',views.search,name='search')
    re_path(r'^api/v1/', include(router.urls)),


    ]

