from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtChapter,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtChapterForm
from django.core.paginator import Paginator
from rest_framework.response import Response

def search(request):
	"""搜索功能"""
	search_name=request.GET.get('search_name')
	error_msg=''

	if not search_name:
		error_msg='请输入关键词'

		return render(request,'learning_logs/index.html',{'error_msg': error_msg})
	articles=Article.objects.filter(art_name__icontains=search_name)
	return render(request,'learning_logs/search_results.html',
		{'error_msg': error_msg,'articles': articles})

from rest_framework.views import APIView
from django.http import HttpResponse

from rest_framework import serializers
import json
class ArtChapterSerializer(serializers.Serializer):
	id=serializers.IntegerField()
	chapter_name=serializers.CharField()
	chapter_content=serializers.CharField()
	article_id=serializers.CharField(source='article.id',read_only=True)
	chapter_add_date=serializers.DateTimeField()

class ArtChapterView(APIView):
	def get(self,request,*args,**kwargs):

		article_id=request.query_params.dict().get('id')
		chapter_idd = request.query_params.dict().get('idd')
		print(chapter_idd)
		article = Article.objects.get(id=article_id)
		artchapter=article.artchapter_set.all()
		ser=ArtChapterSerializer(instance=artchapter,many=True)
		ret=json.dumps(ser.data,ensure_ascii=False)
		# print(type(ret))
		return HttpResponse(ret)
		# return artchapter.get_paginated_response(ser.data)
class ArticleSerializer(serializers.Serializer):
	id=serializers.IntegerField()
	art_name=serializers.CharField()
	art_add_date=serializers.DateTimeField(read_only=True,format="%Y-%m-%d")
	art_author=serializers.CharField()
	user_owner_id=serializers.CharField(source='user_owner.id',read_only=True)
	user_owner_username = serializers.CharField(source='user_owner.username', read_only=True)
	art_type=serializers.CharField()
	art_status=serializers.CharField()
	art_introduction=serializers.CharField()
	art_name_used=serializers.CharField()

	def create(self, validated_data):
		validated_data.update(user_owner_id=1)
		article=Article.objects.create(**validated_data)
		return article
from django.contrib.auth.models import User

from rest_framework.pagination import PageNumberPagination
class ArticleView(APIView):
	def get(self,request,*args,**kwargs):
		article=Article.objects.all()
		pg=MyPageNumberPagination()  #自定义分页对象
		pager_articles = pg.paginate_queryset(queryset=article, request=request, view=self)
		ser = ArticleSerializer(instance=pager_articles, many=True)
		# return Response(ser.data)
		return pg.get_paginated_response(ser.data)

	def post(self,request,*args,**kwargs):
		dat=request.data
		ser=ArticleSerializer(data=dat)
		if ser.is_valid():
			ser.save()
			print('验证成功并保存')
			return HttpResponse(ser.data)
		else:
			print(ser.errors)
			print('验证失败未保存')
			return HttpResponse(ser.errors)
class MyPageNumberPagination(PageNumberPagination):
	page_size = 10
	page_size_query_param = 'size'
	max_page_size = 5
	page_query_param = 'page'

class ChapteContentView(APIView):
	def get(self,request,*args,**kwargs):
		article_id = request.query_params.dict().get('id')
		chapter_idd = request.query_params.dict().get('idd')
		article = Article.objects.get(id=article_id)
		artchapter = article.artchapter_set.all().filter(id=chapter_idd)
		ser=ArtChapterSerializer(instance=artchapter,many=True)
		ret=json.dumps(ser.data,ensure_ascii=False)
		return HttpResponse(ret)



