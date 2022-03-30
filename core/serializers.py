from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import serializers

from system_manage.models import BookItem
from system_manage.serializers import BookItemSerializer

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", 'staff', 'name', 'last_name')
    
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

    def validate_password(self, password):
        if password.islower():
            raise serializers.ValidationError("Should be a least one upper case")
        return password

    def validate_username(self, username):
        if not any(char.isdigit() for char in username):
            raise serializers.ValidationError("Should be a least one digit")
        return username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", 'staff', 'name', 'last_name', 'total_books_checkedout','date_of_membership')
        depth=1
