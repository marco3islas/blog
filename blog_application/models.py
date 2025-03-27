from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.base import django

class Contacto(models.Model):
    name = models.CharField(max_length=80, verbose_name="Nombre")
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title    = models.CharField(max_length=80, verbose_name="Titulo")
    subtitle = models.CharField(max_length=100, verbose_name="Subtitulo", blank=True)
    resumen  = models.CharField(max_length=130, verbose_name="Resumen")
    article  = CKEditor5Field('Text', config_name='extends')

    author   = models.CharField(max_length=20, verbose_name="Autor")
    fecha    = models.DateField()
    image    = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
