from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    def create(self, validated_data):
        return Article.objects.create(**validated_data)