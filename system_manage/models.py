from tkinter import CASCADE
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Author(models.Model):
    name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    description = models.CharField(max_length=255)

    def get_name(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    
    def get_addres(self):
        return self.address

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

class BookItem(models.Model):
    title = models.CharField(max_length=100),
    subject = models.CharField(max_length=100),
    added = models.DateField(),
    published = models.CharField(max_length=50),
    language = models.CharField(max_length=100),
    number_of_pages = models.IntegerField(),
    bar_code = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def checkout(self):
        pass


class Rack(models.Model):
    number : models.ImageField()
    location_identifer: models.CharField(max_length=100)
    book_item : models.ForeignKey(BookItem, on_delete=models.CASCADE)
