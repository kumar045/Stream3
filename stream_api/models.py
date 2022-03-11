from django.db import models

# Create your models here.
class Stream(models.Model):
    stream_text = models.CharField(max_length=1110010000)

    

