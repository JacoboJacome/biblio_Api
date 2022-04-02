from rest_framework import serializers

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
        depth = 1
        
class CreateBookItemSerializer(serializers.ModelSerializer):
    total=serializers.IntegerField()
    class Meta:
        model = BookItem
        fields = ('book','library','rack','total')
        
        
class RentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ('id','book','rent_book','quantity','library','rack')
        # depth=1  
  


