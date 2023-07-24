from django.db import models
from .models import *
# Create your models here.

class Grade(models.Model):
    niveau = models.PositiveIntegerField(help_text = 'Exemple de niveau 1,2,3....')
    Titre = models.CharField( max_length=200, help_text = 'Cellule Informatique , etc')

    def __str__(self):
        return self.Titre
    

class Responsable(models.Model):
    
        Nom = models.CharField(max_length=100)
        Image = models.ImageField( upload_to='user_grade', blank=True, null=True)
        Description = models.CharField( max_length=100)
        titre = models.ForeignKey("Grade", on_delete=models.CASCADE)
    
