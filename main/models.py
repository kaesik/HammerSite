from itertools import chain

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
    availability = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    encumbrance = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ItemWeapon(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    encumbrance = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    damage = models.CharField(max_length=200, null=True)
    is_2h = models.BooleanField(null=True)
    range = models.CharField(max_length=200, null=True)
    qualities_and_flaws = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ItemArmour(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    encumbrance = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    locations = models.CharField(max_length=200, null=True)
    penalty = models.CharField(max_length=200, null=True)
    ap = models.CharField(max_length=200, null=True)
    qualities_and_flaws = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ItemAmmunition(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    encumbrance = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    damage = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=200, null=True)
    range = models.CharField(max_length=200, null=True)
    qualities_and_flaws = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ItemOther(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    encumbrance = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    carries = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


Items = chain(ItemWeapon.objects.all(),
                 ItemArmour.objects.all(),
                 ItemAmmunition.objects.all(),
                 ItemOther.objects.all())