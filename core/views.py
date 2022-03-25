from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

User = get_user_model()

from .serializers import RentBookSerializer, UserSerializer, CreateUserSerializer, RentBookSerializer
from system_manage.models import Book, BookItem
from system_manage.serializers import BookItemSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

    serializer_class = BookItemSerializer

    @action(detail=True, methods=['post','get'])
    def total_books_checkedout(self, request, pk):
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if User.objects.filter(id=pk):
            return Response(print(User.objects.filter(id=pk)))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
