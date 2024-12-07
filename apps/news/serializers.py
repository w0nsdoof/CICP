from rest_framework import serializers

from apps.authentication.models import User
from .models import News, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']

class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = News
        fields = [
            'id', 'title', 'content', 'author', 'summary', 
            'tags', 'created_at', 'updated_at', 
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        new_news = News.objects.create(**validated_data)
        
        if tags_data:
            new_news.tags.set(tags_data)
        
        return new_news

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if tags_data is not None:
            instance.tags.set(tags_data)
        
        instance.save()
        return instance