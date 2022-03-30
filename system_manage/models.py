from tkinter import CASCADE
from uuid import uuid4
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Library(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    
    def get_addres(self):
        return self.address
    
    def __str__(self):
        return self.name

class Rack(models.Model):
    number = models.IntegerField()
    location_identifer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location_identifer

class Author(models.Model):
    name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=255,blank=False)

    def get_name(self):
        return self.name
    
    def __str__(self):
        return (self.name + " " + self.last_name)



class Book(models.Model):
    title = models.CharField(max_length=100,blank=False)
    category = models.CharField(max_length=100,blank=False)
    added = models.DateField(blank=False)
    published = models.DateField(blank=False)
    language = models.CharField(max_length=100,blank=False)
    number_of_pages = models.IntegerField(blank=False)
    author = models.ManyToManyField(Author)

    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    
    
class BookItem(models.Model):
    quantity = models.IntegerField(blank=False)
    codig_UUID = models.UUIDField(default=uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    rent_book = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def checkout(self):
        pass


