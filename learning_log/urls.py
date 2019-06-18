from django.contrib import admin
from django.urls import path, include,re_path

from rest_framework import routers
from learning_logs import views


from django.views.generic import TemplateView

router = routers.DefaultRouter() #路由
router.register(r'article_list', views.ArticleViewSet) #路由地址与接口配置
router.register(r'artchapter_list', views.ArtChapterViewSet)
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('learning_logs.urls')),
    # path('users/', include('users.urls')),

    #vue.js测试页面
    # path('', TemplateView.as_view(template_name="index.html")),

    # re_path(r'^api/v1/', include(router.urls)), #包含进路由配置的url
    path('django/',views.DjangoView.as_view(),name='ddd'),

    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        #浏览器测试接口配置
]
