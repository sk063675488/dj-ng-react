from rest_framework import serializers
from ..models import article_model 

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article_model
        fields = ('name', 'content','descs')