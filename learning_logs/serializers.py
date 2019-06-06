from .models import Article
from django.contrib.auth.models import User, Group
from rest_framework import serializers

#serializers定义api的表现形式
class ArticleSerializers(serializers.HyperlinkedModelSerializer):
	#使用ModelSerializer序列化model模型
	class Meta:
		model=Article #指定序列化的模型
		fields=('art_name','art_author','art_type','art_status','art_introduction')
		#指定要序列化得字段


