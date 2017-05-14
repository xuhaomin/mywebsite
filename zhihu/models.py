from django.db import models


class Daily(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    update_time = models.DateField()
    title = models.CharField(max_length=60)
    img = models.URLField()


class Explore(models.Model):
    aid = models.CharField(max_length=20, primary_key=True, unique=True)
    qid = models.CharField(max_length=20)
    title = models.CharField(max_length=60)
    update_time = models.DateField()
    abstract = models.CharField(max_length=100)
    full_content = models.TextField()
    author = models.CharField(max_length=20)
    day = models.NullBooleanField(default=False)
    month = models.NullBooleanField(default=False)
    reco = models.NullBooleanField(default=False)

class Article(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    title = models.CharField(max_length=60)
    update_time = models.DateField()
    abstract = models.CharField(max_length=100)
    full_content = models.TextField()
    author = models.CharField(max_length=20)

