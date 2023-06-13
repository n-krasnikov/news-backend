from django.db import models

# Create your models here.
class User(models.Model):
    '''User model'''
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField()

class Post(models.Model):
    '''Post model'''
    title = models.CharField(max_length=255)
    text = models.CharField()
    tags = models.CharField(max_length=255)
    image = models.CharField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)