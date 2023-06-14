from django.db import models
from .user import User

class Post(models.Model):
    '''Post model'''
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)