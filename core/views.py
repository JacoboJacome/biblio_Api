from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

User = get_user_model()

from core.serializers import RentBookSerializer, UserSerializer, CreateUserSerializer
from system_manage.models import Book, BookItem
from system_manage.serializers import BookItemSerializer, BookSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

    @action(detail=True)
    def total_books_checkedout(self, request, *arg, **kwargs):
        print(request.data)
        books = BookItem.objects.all()
        serializer = RentBookSerializer(books, many=True)
        return Response(serializer.data, status=200)
     
class BooksUser(ModelViewSet):
    serializer_class = RentBookSerializer
    queryset = BookItem.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return RentBookSerializer
        return UserSerializer 
