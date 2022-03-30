
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import AuthorSerializer, CreateBookSerializer, BookItemSerializer, BookSerializer, CreateBookItemSerializer, LibrarySerializer, RackSerializer, RentBookSerializer
from .models import Book, Author, BookItem, Library, Rack

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
        return RentBookSerializer
    