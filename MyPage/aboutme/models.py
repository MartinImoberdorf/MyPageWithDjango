from django.db import models

# Create your models here.

class AboutMe(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to='aboutme')
    descarga=models.FileField()
    created=models.DateTimeField(auto_now_add=True) #fecha de creación
    update=models.DateTimeField(auto_now_add=True) #fecha de modificación
    

    #vimos doc de model Meta https://docs.djangoproject.com/en/4.0/ref/models/options/

    #El nombre que tendra en la BBDD
    class Meta:
        verbose_name='aboutme'
        verbose_name_plural='aboutmes'
    
    def __str__(self):
        return self.titulo