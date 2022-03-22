from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

User = get_user_model()

from core.serializers import UserSerializer, CreateUserSerializer
from rest_framework.decorators import action

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

        #Frailejon Ernesto Perez