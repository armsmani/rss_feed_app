from django.db import models
from mongoengine import *
from django_mongodb_engine.contrib import MongoDBManager
from django.conf import settings

class News(models.Model):  
    title = models.CharField(max_length = 300)  
    content = models.TextField()  
