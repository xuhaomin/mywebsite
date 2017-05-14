from django.db import models


class Video(models.Model):
    """docstring for Video"""
    title = models.CharField(max_length=100)
    update_time = models.DateField()
    vid = models.CharField(max_length=20, primary_key=True, unique=True)
    img = models.URLField()
    rank = models.IntegerField(null=True, default=100)
    label = models.CharField(max_length=64, null=True)
    series = models.CharField(max_length=64, null=True)
    category = models.CharField(max_length=20, null=True)
