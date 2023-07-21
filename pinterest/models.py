from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class User(User):
  name = models.CharField(max_length=30)
  age = models.IntegerField(default=0)
  GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),]
  color = models.CharField(max_length=1, choices=GENDER)

class Post(models.Model):
  post = models.CharField(max_length=200)
  user_post = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)
  area = models.CharField(max_length=300, null=True, blank=True)

class Comments(models.Model):
  user_comment = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
  comments = models.CharField(max_length=300, null=True, blank=True)
  show_comments = models.BooleanField(default=True)
  
