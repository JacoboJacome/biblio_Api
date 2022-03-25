from tkinter import CASCADE
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

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
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    added = models.DateField()
    published = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    author = models.ManyToManyField(Author)

    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

class Rack(models.Model):
    number = models.IntegerField()
    location_identifer = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.number)
    
    
class BookItem(models.Model):
    cuantity = models.IntegerField()
    bar_code = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    
    def checkout(self):
        pass


