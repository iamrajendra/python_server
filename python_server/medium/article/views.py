from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response({"articles": serializer.data})
    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
    
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
           article_saved = serializer.save()
           return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
    
    def delete(self, request, pk):
    # Get object with this pk
       article = get_object_or_404(Article.objects.all(), pk=pk)
       article.delete()
       return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)