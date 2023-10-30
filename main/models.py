from itertools import chain

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Item(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    group = models.CharField(null=True)
    source = models.CharField(null=True)
    availability = models.CharField(null=True)
    description = models.CharField(null=True)
    encumbrance = models.CharField(null=True)
    price = models.CharField(null=True)

    type = models.CharField(null=True, default=None)
    damage = models.CharField(null=True, default=None)
    is_2h = models.BooleanField(null=True, default=None)
    range = models.CharField(null=True, default=None)
    qualities_and_flaws = models.CharField(null=True, default=None)

    locations = models.CharField(null=True, default=None)
    penalty = models.CharField(null=True, default=None)
    ap = models.CharField(null=True, default=None)

    quantity = models.CharField(null=True, default=None)

    carries = models.CharField(null=True, default=None)

    def __str__(self):
        return self.name


class QualityFlaw(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    group = models.CharField(null=True)
    quality_or_flaw = models.CharField( null=True)
    source = models.CharField(null=True)
    description = models.CharField(null=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    description = models.CharField(null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    attribute = models.CharField(null=True)
    basic_advance = models.CharField(null=True)
    grouped = models.BooleanField(null=True)
    description = models.CharField(null=True)
    specialization = models.CharField(null=True, default=None)
    source = models.CharField(null=True)

    def __str__(self):
        return self.name


class Talent(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    max = models.CharField(null=True)
    tests = models.CharField(null=True, default=None)
    description = models.CharField(null=True)
    source = models.CharField(null=True)

    def __str__(self):
        return self.name


class Race(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    description = models.CharField(null=True)
    opinions = models.CharField(null=True)
    source = models.CharField(null=True)

    weapon_skill = models.CharField(null=True)
    ballistic_skill = models.CharField(null=True)
    strength = models.CharField(null=True)
    toughness = models.CharField(null=True)
    agility = models.CharField(null=True)
    dexterity = models.CharField(null=True)
    intelligence = models.CharField(null=True)
    willpower = models.CharField(null=True)
    fellowship = models.CharField(null=True)
    wounds = models.CharField(null=True)
    fate_points = models.CharField(null=True)
    resilience = models.CharField(null=True)
    extra_points = models.CharField(null=True)
    movement = models.CharField(null=True)

    skills = models.CharField(null=True)
    talents = models.CharField(null=True)

    forenames = models.CharField(null=True, default=None)
    surnames = models.CharField(null=True, default=None)
    clans = models.CharField(null=True, default=None)
    epithets = models.CharField(null=True, default=None)

    age = models.CharField(null=True, default=None)
    eye_colour = models.CharField(null=True, default=None)
    hair_colour = models.CharField(null=True, default=None)
    height = models.CharField(null=True, default=None)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    description = models.CharField(null=True)
    trappings = models.CharField(null=True)

    def __str__(self):
        return self.name


class CareerPath(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    status = models.CharField(null=True)
    skills = models.CharField(null=True)
    talents = models.CharField(null=True)
    trappings = models.CharField(null=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True)
    class_name = models.CharField(null=True)
    limitations = models.CharField(null=True)
    summary = models.CharField(null=True)
    description = models.CharField(null=True)
    advance_scheme = models.CharField(null=True)
    career_path = models.CharField(null=True)
    quotations = models.CharField(null=True)
    adventuring = models.CharField(null=True)
    source = models.CharField(null=True)

    def __str__(self):
        return self.name
