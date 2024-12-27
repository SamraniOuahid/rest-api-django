from .models import BlogPost
from rest_framework import serializers
from django.http import JsonResponse
import json

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields =  ["id", "title", "content", "published_date"]