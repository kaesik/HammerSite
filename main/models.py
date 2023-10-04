from itertools import chain

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Item(models.Model):
    id = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256, null=True)
    group = models.CharField(max_length=256, null=True)
    source = models.CharField(max_length=256, null=True)
    availability = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    encumbrance = models.CharField(max_length=256, null=True)
    price = models.CharField(max_length=256, null=True)

    type = models.CharField(max_length=256, null=True, default=None)
    damage = models.CharField(max_length=256, null=True, default=None)
    is_2h = models.BooleanField(null=True, default=None)
    range = models.CharField(max_length=256, null=True, default=None)
    qualities_and_flaws = models.CharField(max_length=256, null=True, default=None)

    locations = models.CharField(max_length=256, null=True, default=None)
    penalty = models.CharField(max_length=256, null=True, default=None)
    ap = models.CharField(max_length=256, null=True, default=None)

    quantity = models.CharField(max_length=256, null=True, default=None)

    carries = models.CharField(max_length=256, null=True, default=None)

    def __str__(self):
        return self.name
