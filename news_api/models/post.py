from django.db import models
from .user import User
from django.conf import settings

class Post(models.Model):
    '''Post model'''
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)