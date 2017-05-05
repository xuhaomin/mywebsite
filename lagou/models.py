from django.db import models


class Position(models.Model):
    """docstring for Position"""
    pid = models.CharField(max_length=20,primary_key=True, unique=True)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    stage = models.CharField(max_length=10)
    requirement = models.TextField()
    benefit = models.CharField(max_length=50)
    salary = models.CharField(max_length=10)
    labels = models.CharField(max_length=40)
    catagory = models.CharField(max_length=30, null=True)
    companylink = models.URLField(null=True)