from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings

from ..managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    avatar = models.CharField(null=True)
    password = models.CharField(max_length=255)

    @property
    def last_login(self): return None

    @property
    def is_superuser(self): return False


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["avatar", "username"]

    objects = UserManager()

    def __str__(self):
        return self.email
    