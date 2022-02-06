from unicodedata import name
from django.db import models

# Create your models here.
class Stream(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    uri = models.ImageField()

    

