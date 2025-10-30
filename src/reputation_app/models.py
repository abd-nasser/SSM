from django.db import models

class CategoriePreuve(models.Model):
    name = models.CharField(max_length=100) #trophée or recompense ; partenariats, certificat or attestation, mediaTV
    icone = models.CharField(max_length=50, blank=True)
    ordre = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class PreuveSociale(models.Model):
    categorie = models.ForeignKey(CategoriePreuve, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to="preuves/")
    date_obtention = models.DateField()
    description = models.TextField(blank=True)
    ordre_affichage= models.IntegerField(default=0)
