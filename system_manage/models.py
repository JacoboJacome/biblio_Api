from tkinter import CASCADE
from uuid import uuid4
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Author(models.Model):
    name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=255,blank=False)

    def get_name(self):
        return self.name
    
    def __str__(self):
        return (self.name + " " + self.last_name)

class Library(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    
    def get_addres(self):
        return self.address
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100,blank=False)
    category = models.CharField(max_length=100,blank=False)
    added = models.DateField(blank=False)
    published = models.CharField(max_length=50,blank=False)
    language = models.CharField(max_length=100,blank=False)
    number_of_pages = models.IntegerField(blank=False)
    author = models.ManyToManyField(Author)

    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

class Rack(models.Model):
    number = models.IntegerField(blank=False)
    description = models.CharField(max_length=50, blank=False)
    location_identifer = models.CharField(max_length=100,blank=False)
    
    def __str__(self):
        return (str(self.number) + " " + self.description)
    
    
class BookItem(models.Model):
    cuantity = models.IntegerField(blank=False)
    bar_code = models.CharField(max_length=100,blank=False)
    codig_UUID = models.UUIDField(default=uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    
    def checkout(self):
        pass


