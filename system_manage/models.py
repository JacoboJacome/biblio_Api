from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.


class Users(models.Model):
    pass


class Books(models.Model):
    pass
