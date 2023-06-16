from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from ..managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True)
    avatar = models.CharField()

    @property
    def last_login(self): return None

    @property
    def is_superuser(self): return False

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "email"]

    objects = UserManager()

    def __str__(self):
        return self.username
