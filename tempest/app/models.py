from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=100)
    Turma = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Representante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Turma = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

