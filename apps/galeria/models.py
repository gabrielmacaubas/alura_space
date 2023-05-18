from django.db import models
from datetime import datetime


class Categoria(models.Model):
    categoria = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.categoria


class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.ForeignKey('galeria.Categoria', on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )


    def __str__(self):
        return self.nome
