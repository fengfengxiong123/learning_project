from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtChapter,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtChapterForm
from django.core.paginator import Paginator

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
		artchapter=ArtChapter.objects.all()
		ser=ArtChapterSerializer(instance=artchapter,many=True)
		ret=json.dumps(ser.data,ensure_ascii=False)
		print(type(ret))
		return HttpResponse(ret)

class ArticleSerializer(serializers.Serializer):
	id=serializers.IntegerField()
	art_name=serializers.CharField()
	art_add_date=serializers.DateTimeField(read_only=True)
	art_author=serializers.CharField()
	user_owner_id=serializers.CharField(source='user_owner.id',read_only=True)
	user_owner_username = serializers.CharField(source='user_owner.username', read_only=True)
	art_type=serializers.CharField()
	art_status=serializers.CharField()
	art_introduction=serializers.CharField()

class ArticleView(APIView):
	def get(self,request,*args,**kwargs):
		article=Article.objects.all()
		ser=ArticleSerializer(instance=article,many=True)
		ret=json.dumps(ser.data,ensure_ascii=False)
		return HttpResponse(ret)
