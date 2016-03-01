from django.db import models
from mongoengine import *
from django_mongodb_engine.contrib import MongoDBManager
from django.conf import settings


class RssDetails(models.Model):
    link = models.TextField()
    created_date = models.CharField(max_length=20)


class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    link = models.TextField()
    published_date = models.CharField(max_length=300)
    language = models.CharField(max_length=100)