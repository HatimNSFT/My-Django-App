from django.db import models

# Create your models here.

class Tours(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    img  = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)