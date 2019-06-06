from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Article,ArtContent,ArtLabel,ArtHot,ArtDiscuss
from . forms import ArticleForm,ArtContentForm

from rest_framework import viewsets
from learning_logs.serializers import ArticleSerializers

def index(request):
	"""主页（文章列表页）"""
	articles=Article.objects.order_by('art_add_date')
	context={'articles':articles}
	return render(request,'learning_logs/index.html',context)
	# return render(request,'article/list.html',context)

def article(request,article_id):
	"""文章详情页，具体单页"""
	article=Article.objects.get(id=article_id)
	artcontents=article.artcontent_set.all()	
	context = {'article':article,'artcontents':artcontents}
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
			new_article.art_owner=request.user
			new_article.save()
			return HttpResponseRedirect(reverse('learning_logs:index'))
	context ={'form':form}
	return render(request,'learning_logs/new_article.html',context)

@login_required
def edit_art_content(request,article_id):
	"""修改文章标题等内容"""
	article = Article.objects.get(id=article_id)
	art_content =article.artcontent_set.all()
	if article.art_owner != request.user:
		raise Http404
	if request.method != "POST":
		form = ArticleForm(instance=article)
	else:
		form = ArticleForm(instance=article,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:article',
				args=[article.id]))
	context={'article':article,'art_content':art_content,'form':form}
	return render(request,'learning_logs/edit_art_content.html',context)

@login_required
def new_chapter(request,article_id):
	article = Article.objects.get(id=article_id)
	art_content=article.artcontent_set.all()
	if article.art_owner != request.user:
		raise Http404	
	if request.method !='POST':
		form=ArtContentForm()		
	else:
		#post的表单中外键article字段为null	
		form=ArtContentForm(request.POST)

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
	artcontents=ArtContent.objects.get(id=chapter_id)	
	context={'artcontents':artcontents}
	return render(request,'learning_logs/look_chapter.html',context)

@login_required
def edit_chapter(request,article_id,chapter_id):
	#实例化具体一片文章
	article=Article.objects.get(id=article_id)
	#实例化具体的一章内容
	artcontent=ArtContent.objects.get(id=chapter_id)
	# """修改章节内容"""
	if article.art_owner!=request.user:
		raise Http404
	if request.method != 'POST':
		form=ArtContentForm(instance=artcontent)
	else:
		form=ArtContentForm(instance=artcontent,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:look_chapter',
				args=[artcontent.id]))
	context ={'artcontent':artcontent,'form':form,'article':article}
	
	
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

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all() #集合
    serializer_class = ArticleSerializers  #序列化