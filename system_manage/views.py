
from core import serializers
from core.serializers import RentBookSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


from system_manage.serializers import AuthorSerializer, CreateBookSerializer, BookItemSerializer, BookSerializer, CreateBookItemSerializer, RentBookSerializer
from .models import Book, Author, BookItem

class CatalogLibrary(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','author','published','category']
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookSerializer   
        return BookSerializer

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


class RentBook(ModelViewSet):
    serializer_class = BookItemSerializer
    queryset = BookItem.objects.all()

    def get_serializer_class(self):
        if self.action == "partial_update":
            serializer_class = RentBookSerializer
        return BookItemSerializer
    
    @action(detail=True, methods = ['PUT','GET'])
    def rent_book(self,request,pk):
        return Response ( print(request.data) )
    
    # @action(detail=True, methods=['put'])
    # def rent_book(self, request, pk):
    #     book = self.get_object()
    #     serializer = RentBookSerializer
    #     if serializer.is_valid():
    #         book.rent_book(serializer.validated_data['cuantity'])
    #         book.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 