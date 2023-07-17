from django.db import models
from django.conf import settings

from .user import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)