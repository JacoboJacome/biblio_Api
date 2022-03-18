from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    description = models.CharField(max_length=255)

    def get_name(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100),
    subject = models.CharField(max_length=100),
    added = models.DateField(),
    published = models.CharField(max_length=50),
    language = models.CharField(max_length=100),
    number_of_pages = models.IntegerField(),
    author = models.ManyToManyField(Author)

    def get_title(self):
        return self.title

