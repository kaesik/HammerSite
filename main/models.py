from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Item(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
