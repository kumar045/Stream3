from django.db import models

# Create your models here.
class Stream(models.Model):
    stream_id = models.IntegerField(max_length=1000)
    

