from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtChapter,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtChapterForm


from django.core.paginator import Paginator

def index(request):
	"""主页（文章列表页）"""
	articles=Article.objects.order_by('art_add_date')
	context={'articles':articles}
	return render(request,'learning_logs/index.html',context)
	# return render(request,'article/list.html',context)

def article(request,article_id):
	"""文章详情页，具体单页"""
	article=Article.objects.get(id=article_id)
	artchapters=article.artchapter_set.all()
	
	paginator=Paginator(artchapters,10)
	current_page=int(request.GET.get('page',1))
	#分页标签显示7个
	if paginator.num_pages >7 :
		if current_page-3 < 1:
			page_ran=range(1,8)
		elif current_page +3 >paginator.num_pages:
			page_ran=range(paginator.num_pages-6,paginator.num_pages+1)
		else:
			page_ran=range(current_page-3,current_page+4)
		page_range=page_ran
	else:
		page_range=paginator.page_range


	current_page_chapter=paginator.page(current_page)
	context = {'article':article,'current_page_chapter':current_page_chapter,'page_range':page_range}
	return render(request,'learning_logs/article.html',context)

@login_required
def new_article(request):
	"""添加新文章"""
	if request.method != 'POST':
		form = ArticleForm()
	else:
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save(commit=False)
			new_article.user_owner=request.user
			new_article.save()
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context ={'form':form}
	return render(request,'learning_logs/new_article.html',context)

@login_required
def edit_art_chapter(request,article_id):
	"""修改文章标题等内容"""
	article = Article.objects.get(id=article_id)
	artchapter =article.artchapter_set.all()
	if article.user_owner != request.user:
		raise Http404
	if request.method != "POST":
		form = ArticleForm(instance=article)
	else:
		form = ArticleForm(instance=article,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:article',
				args=[article.id]))
	context={'article':article,'artchapter':artchapter,'form':form}
	return render(request,'learning_logs/edit_art_chapter.html',context)

@login_required
def new_chapter(request,article_id):
	article = Article.objects.get(id=article_id)
	art_chapter=article.artchapter_set.all()
	if article.user_owner != request.user:
		raise Http404	
	if request.method !='POST':
		form=ArtChapterForm()		
	else:
		#post的表单中外键article字段为null	
		form=ArtChapterForm(request.POST)

		if form.is_valid:
			#验证成功后需要为外键article字段，设置参数（instance.article）为实例（article）
			form.instance.article=article
			#接受了POST以及article实例后保存
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:article',args=[article_id]))
		else:
			raise Http404
	context={'form':form,'article':article}
	return render(request,'learning_logs/new_chapter.html',context)

def look_chapter(request,chapter_id):
	"""查看具体章节"""		
	artchapters=ArtChapter.objects.get(id=chapter_id)	
	context={'artchapters':artchapters}
	return render(request,'learning_logs/look_chapter.html',context)

@login_required
def edit_chapter(request,article_id,chapter_id):
	#实例化具体一片文章
	article=Article.objects.get(id=article_id)
	#实例化具体的一章内容
	artchapter=ArtChapter.objects.get(id=chapter_id)
	# """修改章节内容"""
	if article.user_owner!=request.user:
		raise Http404
	if request.method != 'POST':
		form=ArtChapterForm(instance=artchapter)
	else:
		form=ArtChapterForm(instance=artchapter,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:look_chapter',
				args=[artchapter.id]))
	context ={'artchapter':artchapter,'form':form,'article':article}
	
	
	return render(request,'learning_logs/edit_chapter.html',context)
	
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

#方法一
# class ArticleSerializer(serializers.Serializer):
# 	art_name=serializers.CharField()
# import json
# from learning_logs import models
# class ArticleView(APIView):
# 	def get(self,request,*args,**kwargs):
# 		articles=models.Article.objects.all()
# 		ser=ArticleSerializer(instance=articles,many=True)
# 		ret=json.dumps(ser.data,ensure_ascii=False)
# 		return HttpResponse(ret)

#方法二：使用ModelSerializer类
from learning_logs import models
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Article
		# fields='__all__'
		# depth=1
		# fields=['art_name','art_add_date','art_author','user_owner','art_type','art_status','art_introduction']
		fields=['art_name','user_owner']
import json
class ArticleView(APIView):
	def get(self,request,*args,**kwargs):
		articles=models.Article.objects.all()
		ser=ArticleSerializer(instance=articles,many=True)
		ret=json.dumps(ser.data,ensure_ascii=False)

		return HttpResponse(ret)

	def post(self,request,*args,**kwargs):
		ser =ArticleSerializer(data=request.data)
		if ser.is_valid():
			article=ser.save()
			user_owner=models.Article.objects.filter(id__in=request.data['user_owner'])
			article.user_owner=user_owner
			
			return HttpResponse(ser.data)
		else:
			
			return HttpResponse(ser.errors)
