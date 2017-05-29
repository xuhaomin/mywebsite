from django.db import models

# Create your models here.

class Slogan(models.Model):
    """docstring for Video"""
    text = models.CharField(max_length=150)
    by = models.CharField(max_length=64, null=True)
