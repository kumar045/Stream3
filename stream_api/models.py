from django.db import models

# Create your models here.
class Stream(models.Model):
    stream_bytes = models.CharField(max_length=1000000000000000000000000000000000000000000000000000000000)
    

