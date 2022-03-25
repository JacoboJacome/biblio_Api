from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import models

from .models import Book, Author, BookItem

        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'last_name', 'description')
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
        
class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'category', 'added', 'published', 'language', 'number_of_pages', 'author')
        
class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = '__all__'
        depth = 2
        
class CreateBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ('cuantity', 'bar_code','book','library','rack')
        
class RentBookSerializer(serializers.Serializer):
    class Meta:
        model = BookItem
        fields = ('cuantity',)