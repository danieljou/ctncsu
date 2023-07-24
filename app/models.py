from django.db import models

from django.utils.text import slugify
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

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
        
class Article(models.Model):
    Titre  = models.CharField( max_length=255)
    Banniere = models.ImageField("Banière", upload_to='Banieres')
    contetu = RichTextUploadingField()
    created_date = models.DateField(auto_now_add=True)

    slug = models.SlugField(blank=True, unique = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Titre)
        super(Article, self).save(*args, **kwargs)