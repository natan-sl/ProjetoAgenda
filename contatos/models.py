from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=12)  # tamanho maximo que o nome vai receber
    sobrenome = models.CharField(max_length=15, blank=True)  # O blank faz com que o sobrenome seja opcional
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=35, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome
