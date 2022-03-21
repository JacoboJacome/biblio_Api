from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    e_mail = models.EmailField(blank=False)
    password = models.CharField(max_length=255, blank=False)
    staff = models.BooleanField(default=False, blank=False)
    user_name = models.ForeignKey(User, blank=False, max_length=50)
    date_of_membership: models.DateField()
    total_books_checkedout: models.IntegerField()
    
    def add_book_item(self):
        pass
    
    def block_member(self):
        pass
    
    def unblock_member(self):
        pass
    
    def get_total_checkedout_books(self):
        pass
    
    def reset_password(self):
        pass

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

class BookItem():
    title = models.CharField(max_length=100),
    subject = models.CharField(max_length=100),
    added = models.DateField(),
    published = models.CharField(max_length=50),
    language = models.CharField(max_length=100),
    number_of_pages = models.IntegerField(),
    book = models.ManyToManyField(Book)
    bar_code = models.CharField(max_length=100)
    library = models.ManyToOneRel(Library)
    
    def checkout(self):
        pass


class Rack():
    number : models.ImageField()
    location_identifer: models.CharField(max_length=100)
    book_item : models.ManyToOneRel(BookItem)