from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


from system_manage.serializers import AuthorSerializer, BookSerializer, BookItemSerializer, CatalogSerializer, CreateBookItemSerializer
from .models import Book, Author, BookItem

class CatalogLibrary(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','author','published','category']
    
    def get_serializer_class(self):
        if self.action == "create":
            return BookSerializer
        return CatalogSerializer

class CreateAuthor(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return AuthorSerializer
        return AuthorSerializer
    
class GetBookItem(ModelViewSet):
    serializer_class = BookItemSerializer
    queryset = BookItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookItemSerializer
        return BookItemSerializer
