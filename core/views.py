from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

User = get_user_model()

from .serializers import UserSerializer, CreateUserSerializer
from system_manage.serializers import CatalogSerializer
from system_manage.models import Book

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

class CatalogLibrary2(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Book.objects.all()

    @action(detail=False)
    def published_books(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = self.get_serializer_class()
        serializer = CatalogSerializer(books, many=True)
        return  Response(serializer.data, status=200)