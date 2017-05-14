from django.db import models

# Create your models here.


class Owner(models.Model):
    """docstring for Owner"""
    mid = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    face = models.URLField(null=True)


class Archive(models.Model):
    """docstring for archive"""
    aid = models.CharField(max_length=10, primary_key=True, unique=True)
    title = models.CharField(max_length=80)
    pic = models.URLField(null=True)
    owner = models.ForeignKey(Owner)
    pubdate = models.IntegerField()
