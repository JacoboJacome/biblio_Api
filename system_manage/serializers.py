from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import models

from .models import Book, Author, BookItem, Library, Rack

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
        
class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = '__all__'
        
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
        # depth = 2
        
class CreateBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ('quantity','book','library','rack')
        
class RentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ('book','rent_book','quantity')        

