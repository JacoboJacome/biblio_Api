from itertools import count
from rest_framework import status, permissions
from core import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

#*Imports from system_manage
from .serializers import AuthorSerializer, CreateBookSerializer, BookItemSerializer, BookSerializer, CreateBookItemSerializer, LibrarySerializer, RackSerializer, RentBookSerializer
from .models import Book, Author, BookItem, Library, Rack
from .permissions import IsOwnerOrReadOnly

#*Imports From Core
from core.models import User
from core.serializers import UserSerializer


class CreateLibrary(ModelViewSet):
    serializer_cass = LibrarySerializer
    queryset = Library.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LibrarySerializer
        return LibrarySerializer
    
class CreateRack(ModelViewSet):
    serializer_class = RackSerializer
    queryset = Rack.objects.all()
    
    def get_serializer_class(self):
        if self.action=='create':
            return RackSerializer
        return RackSerializer

class CreateAuthor(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return AuthorSerializer
        return AuthorSerializer
    
class CatalogLibrary(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','author','published','category']
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookSerializer   
        return BookSerializer
    
class CreateBookItem(ModelViewSet):
    serializer_class = BookItemSerializer
    queryset = BookItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookItemSerializer
        return BookItemSerializer

    def create(self,request,*args,**kwargs):
        total = request.data['total']
        models=[]
        for i in range(int(total)):
            serializer = BookItemSerializer(data=request.data)
            if serializer.is_valid():
                models.append(serializer)
                
        save_models=[model.save() for model in models]
        resuls_serializer=BookItemSerializer(save_models,many=True)
        return Response(resuls_serializer.data)

class RentBook(ModelViewSet):
    serializer_class = RentBookSerializer
    queryset = BookItem.objects.all()

    def get_serializer_class(self):
        if self.action == "update":
            return RentBookSerializer
        return BookItemSerializer
    
    def update(self, request, *args, **kwargs):

        if len(BookItem.objects.filter(rent_book=request.data['rent_book'])) <= 5:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        
        else:
            return Response({'error', 'Ya tiene muchos'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    
class GiveOutBook(ModelViewSet):
    serializer_class = BookItemSerializer
    queryset = BookItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == "update":
            return RentBookSerializer
        return BookItemSerializer   
    
        
    def update(self, request,pk, *args, **kwargs):
        
        item = BookItem.objects.get(pk=pk)
        user = item.rent_book.id

        if BookItem.objects.filter(rent_book=user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):

                instance._prefetched_objects_cache = {}

            return Response(serializer.data, status = status.HTTP_200_OK)
        
        else:
            return Response({'error', 'HTTP 400 BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)