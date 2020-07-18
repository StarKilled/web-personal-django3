from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    descripcion = models.TextField(verbose_name ="Descripcion")
    image = models.ImageField(verbose_name = "Imagen",upload_to= "projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name ="Fecha de Creción")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edicion")
    urlfield = models.URLField(verbose_name="Dirrecion Web", null= True, blank = True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
    def __str__(self):
        return self.title