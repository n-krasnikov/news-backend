from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings
import jwt

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
    REQUIRED_FIELDS = ["password", "username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_username(self):
        return self.username

    def _generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk,
        }, settings.SECRET_KEY, algorithm='HS256')

        return token