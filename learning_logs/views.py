from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtChapter,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtChapterForm
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import serializers
import json
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination


#三个序列化
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

class ArtChapterSerializer(serializers.Serializer):
	id=serializers.IntegerField()
	chapter_name=serializers.CharField()
	# chapter_content=serializers.CharField()
	article_id=serializers.CharField(source='article.id',read_only=True)
	chapter_add_date=serializers.DateTimeField()

class ChapteContentSerializer(serializers.Serializer):
	id=serializers.IntegerField()
	chapter_name=serializers.CharField()
	chapter_content=serializers.CharField()
	article_id=serializers.CharField(source='article.id',read_only=True)
	chapter_add_date=serializers.DateTimeField()

#重写分页类，重写参数的名称pageSize（数据量）和pageNum（当前页）
class MyPageNumberPagination(PageNumberPagination):
	page_size_query_param = 'pageSize'
	page_query_param = 'pageNum'

#接口api
class ArticleView(APIView):
	def get(self,request,*args,**kwargs):
		# page_id = request.query_params.dict().get('pageNum')
		search_name=request.GET.get('search_name')
		pageNum=request.GET.get('pageNum')
		pageSize=request.GET.get('pageSize')
		ca=request.GET.get('ca')
		if pageNum or pageSize:
			print(request.GET)
			article=Article.objects.all()
			pg=MyPageNumberPagination()  #自定义分页对象
			pager_articles = pg.paginate_queryset(queryset=article, request=request, view=self)
			ser = ArticleSerializer(instance=pager_articles, many=True)
			ret = {'code': 1000, 'msg': None,'lens': None, 'data': None}
			try:
				ret['msg']='成功'
				ret['data']=ser.data
				ret['lens']=len(article)
			except Exception as e:
				ret['code']=1001
				ret['msg']='失败'
			# return pg.get_paginated_response(ret)
			return Response(ret)
		elif search_name:
			print("zhixing")
			error_msg = ''
			if not search_name:
				error_msg = '请输入关键词'
				print(type(error_msg))
				print(type(json.dumps(error_msg)))
				return HttpResponse(error_msg)
			articles = Article.objects.filter(art_name__icontains=search_name)
			ser = ArticleSerializer(instance=articles, many=True)
			ret = {'code': 1000, 'msg': None,'lens': None, 'data': None}
			try:
				ret['msg']='成功'
				ret['data']=ser.data
				ret['lens']=len(articles)
			except Exception as e:
				ret['code']=1001
				ret['msg']='失败'
			# return pg.get_paginated_response(ret)
			return Response(ret)
		elif ca:
			articles = Article.objects.all().filter(art_type=ca)
			ser = ArticleSerializer(instance=articles, many=True)
			ret = {'code': 1000, 'msg': None, 'lens': None, 'data': None}
			try:
				ret['msg'] = '成功'
				ret['data'] = ser.data
				ret['lens'] = len(articles)
			except Exception as e:
				ret['code'] = 1001
				ret['msg'] = '失败'
			return Response(ret)
		else:
			ret='无效请求'
			return HttpResponse(ret)
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

class ArtChapterView(APIView):
	def get(self,request,*args,**kwargs):
		article_id=request.query_params.dict().get('id')
		print(article_id)
		article = Article.objects.get(id=article_id)
		artchapter=article.artchapter_set.all()
		# print(artchapter)
		ser=ArtChapterSerializer(instance=artchapter,many=True)
		ret={'code':1000,'msg':None,'lens':None,'data':None}
		try:
			ret['msg']='成功'
			ret['lens']=len(artchapter)
			ret['data']=ser.data
		except Exception as e:
			ret['code']=1001
			ret['msg']='失败'
		return Response(ret)
		# return artchapter.get_paginated_response(ser.data)

class ChapteContentView(APIView):
	def get(self,request,*args,**kwargs):
		article_id = request.query_params.dict().get('id')
		chapter_idd = request.query_params.dict().get('idd')
		article = Article.objects.get(id=article_id)
		artchapter = article.artchapter_set.all().filter(id=chapter_idd)
		ser=ChapteContentSerializer(instance=artchapter,many=True)
		ret={'code':1000,'msg':None,'lens':None,'data':None}
		try:
			ret['msg']='成功'
			ret['data']=ser.data
			ret['lens']=len(artchapter)
		except Exception as e:
			ret['code']=1001
			ret['msg']='失败'
		return Response(ret)








