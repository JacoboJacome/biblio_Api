from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Book

      
class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subject', 'published', 'author')
        depth = 1
        

