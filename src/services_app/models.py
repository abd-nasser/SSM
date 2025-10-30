from django.db import models
from auth_app.models import Client

class Categories(models.Model):
    name = models.CharField(max_length=100)
    


      
class Services(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="services_images/", blank=True, null=True)
    ref = models.TextField(null=True, blank=True)
    descriptions = models.TextField(blank=True)
    categories = models.ForeignKey(Categories,
                                   related_name="cat",
                                   on_delete=models.CASCADE)
    
class Realisation(models.Model):
    image = models.ImageField(upload_to="realisation_image/", blank=True, null=True)
    date = models.DateField(null=True)
    localisation = models.CharField(max_length=150)

    
class Commentaire(models.Model):
    clients = models.ForeignKey(Client, 
                                on_delete=models.PROTECT)
    realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    