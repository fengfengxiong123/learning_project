from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField #富文本
#一对多
#User（系统自带）--Article（表1）
#Article（表1）--ArtChapter（表2）
#Article（表1）--ArtLabel（表3）
#Article（表1）--ArtDiscuss（表5）
#User（系统自带）--ArtDiscuss（表5）
#一对一
#Article（表1）--ArtHot（表4）??
class Article(models.Model):
	"""文章表（表1）"""
	art_name=models.CharField('标题',max_length=200)
	art_add_date=models.DateTimeField(auto_now_add=True)
	art_author=models.CharField('作者',max_length=10,default="")
	user_owner=models.ForeignKey(User,on_delete=models.CASCADE)
	type_choices=[
		('流行',(
<<<<<<< HEAD
			('1','玄幻'),
			('2','奇幻'),
			('3','科幻'),
			('4','武侠'),
			('5','仙侠'),
			('5','都市'),
			('6','言情'),
			('7','历史'),
			)
		),
		('经典',(
			('1','名著'),
			('2','神话'),
			('3','小说'),
			('4','诸子'),
			('5','诗词'),
			('6','史书'),
			)
		),
	]
	art_type=models.CharField(max_length=20,choices=type_choices)
=======
			('xuanhuan','玄幻'),
			('qihuan','奇幻'),
			('kehuan', '科幻'),
			('wuxia', '武侠'),
			('xianxia', '仙侠'),
			('dushi', '都市'),
			('yanqing', '言情'),
			('lishi', '历史'),
		) ),
		('经典',(
			('mingzhu','名著'),
			('shenhua','神话'),
			('xiaoshuo','小说'),
			('zhuzi','诸子'),
			('shici','诗词'),
			('shishu','史书'),
		))
	]
	art_type=models.CharField(max_length=200,choices=type_choices)
>>>>>>> 39d9e35ed34b51df628f65b8c889f3ab4138f734
	art_status=models.CharField('状态',max_length=200,default="")
	art_introduction=models.CharField('简介',max_length=200,default="")
	art_name_used=models.CharField('曾用名',max_length=200,default="")

	class Meta:
		ordering = ['art_add_date']
		
	def __str__(self):
		if len(self.art_name)>=20:
			art_name_limit=self.art_name[:20]+'...'
		else:
			art_name_limit=self.art_name
			#限制返回文章名字符数
		return art_name_limit 

class ArtChapter(models.Model):
	"""文章章节内容表(表2）"""	
	chapter_name=models.CharField('章名',max_length=200)
	chapter_content=HTMLField('文章内容')
	article=models.ForeignKey(Article,verbose_name="文章",on_delete=models.CASCADE,null=True)
	chapter_add_date=models.DateTimeField(auto_now=True)
	class Meta:
		ordering=['chapter_add_date']

	
class ArtLabel(models.Model):
	"""标签内容表（表3）"""
	label_content=models.CharField('标签',max_length=20)
	article=models.ForeignKey(Article,on_delete=models.CASCADE)

class ArtHot(models.Model):
	"""文章热度表（表4）"""
	hot_evaluate=models.BigIntegerField('评价值',null=True,blank=True)
	hot_browse=models.BigIntegerField('浏览量',null=True,blank=True)
	hot_relay=models.BigIntegerField('转发数',null=True,blank=True)
	hot_share=models.BigIntegerField('分享数',null=True,blank=True)
	hot_discuss=models.BigIntegerField('讨论值',null=True,blank=True)
	article=models.OneToOneField(Article,on_delete=models.CASCADE)

class ArtDiscuss(models.Model):
	"""文章讨论表（表5)"""
	discuss_content=models.TextField('留言内容')
	discuss_add_date=models.DateTimeField(auto_now=True)
	discuss_owner=models.ForeignKey(User,on_delete=models.CASCADE)
	article=models.ForeignKey(Article,on_delete=models.CASCADE)
	



	



