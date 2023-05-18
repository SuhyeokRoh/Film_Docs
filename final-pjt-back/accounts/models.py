from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nick_name = models.CharField(max_length=15)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
