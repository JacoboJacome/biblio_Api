from django.contrib.auth import get_user_model
from rest_framework import serializers
from system_manage.models import UserProfile

User = get_user_model()

class LibrianUser(serializers.ModelSerializer):
    class Meta:
        model : UserProfile
        fields = ('name', 'last_mame','staff', 'user_name','id')

class MemberUser(serializers.ModelSerializer):
    class Meta:
        model : UserProfile
        fields = ('name', 'last_mame','staff','user_name','date_of_membership','id')