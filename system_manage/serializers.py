from django.contrib.auth import get_user_model
from rest_framework import serializers
from system_manage.models import UserProfile

User = get_user_model()

class Librian(serializers.ModelSerializer):
    class Meta:
        model : UserProfile
        fields = ('name', 'last_mame','staff', 'user_name','id')

class Member(serializers.ModelSerializer):
    class Meta:
        model : UserProfile
        fields = ('name', 'last_mame','staff','user_name','date_of_membership','id')