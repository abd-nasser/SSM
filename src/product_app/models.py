from django.db import models
from django.contrib.auth.models import AbstractUser



class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField(default=0)
    stoks =  models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    promos = models.BooleanField(default=False)
    
   