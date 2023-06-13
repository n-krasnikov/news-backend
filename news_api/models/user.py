from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''User model'''
    avatar = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    class Meta:
        ordering = ['id']
        unique_together = ['email', 'username']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
