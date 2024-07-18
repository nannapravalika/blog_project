from rest_framework import serializers
from .models import Post, Comment

from rest_framework_simplejwt.serializers import TokenRefreshSerializer,TokenObtainPairSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_date']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'published_date', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
 

class ObtainTokenSerializer(TokenObtainPairSerializer):
    pass  # No need to add any fields or methods unless customization is required


class RefreshTokenSerializer(TokenRefreshSerializer):
    pass  # No need to add any fields or methods unless customization is required
