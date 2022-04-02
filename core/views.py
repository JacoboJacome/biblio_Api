from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

#*Imports from Core
from .serializers import  UserSerializer, CreateUserSerializer
User = get_user_model()

#*Imports from system_manage
from system_manage.models import BookItem
from system_manage.serializers import BookItemSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

    @action(detail=True)
    def total_books_checkedout(self, request, *arg,**kwargs):
        books = BookItem.objects.filter(rent_book=self.kwargs["pk"])
        serializer = BookItemSerializer(books, many=True)
        return Response(serializer.data, status=200)