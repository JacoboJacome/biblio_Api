from locale import normalize
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from system_manage.models import BookItem

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, last_name=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, name=None, last_name=None):
        user = self.create_user(
            email, name, last_name, password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        user = self.create_user(
            email, password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    cellphone = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_membership = models.DateField(auto_now_add=True)
    total_books_checkedout = models.IntegerField(default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email + " " + self.name
    
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
    
    def get_full_name(self):
        return self.name

    def has_module_perms(self, perm, obj=None):
        return True


    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_admin(self):
        return  self.admin

    @property
    def is_staff(self):
        return self.staff

    def __str__(self):
        return self.email
