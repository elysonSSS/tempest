from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Curso(models.Model):
    nomecurso =  models.CharField(max_length=100, verbose_name="Nome do curso", unique=True)
    professores = models.ManyToManyField(User, related_name="professores")
    def __str__(self):
        return self.nomecurso

SEMESTRES_CHOICES = {
    "1 SEMESTRE": "1 SEMESTRE",
    "2 SEMESTRE": "2 SEMESTRE",
    "3 SEMESTRE": "3 SEMESTRE",
    "4 SEMESTRE": "4 SEMESTRE",
    "5 SEMESTRE": "5 SEMESTRE",
    "6 SEMESTRE": "6 SEMESTRE",
    "7 SEMESTRE": "7 SEMESTRE",
    "8 SEMESTRE": "8 SEMESTRE",
    "9 SEMESTRE": "9 SEMESTRE",
    "10 SEMESTRE": "10 SEMESTRE",
}


class SubstituicaoAula(models.Model):
    HORARIOS_CHOICES = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
    }

    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_solicitadas', verbose_name='Solicitante')
    data_hora_solicitacao = models.DateTimeField(default=timezone.now)
    data_hora_aula_substituida = models.DateField(verbose_name='Data da Aula a ser Substituída')
    horarios_aula = models.IntegerField(choices=HORARIOS_CHOICES)
    curso_afetado = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso Afetado')
    semestre_afetado = models.CharField(max_length=60,choices=SEMESTRES_CHOICES)

    def __str__(self):
        return f'{self.solicitante.username} - {self.data_hora_aula_substituida}'

    class Meta:
        verbose_name = 'Substituição de Aula'
        verbose_name_plural = 'Substituições de Aula'

class AceiteSubs(models.Model):
    substituto_nome = models.ForeignKey(User, on_delete=models.CASCADE, max_length=255, verbose_name='Nome do Substituto')
    solicitacao = models.ForeignKey(SubstituicaoAula, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.substituto_nome} - {self.solicitacao.data_hora_aula_substituida}'



class Representante(models.Model):
    nomerepresentante = models.CharField(max_length=120, verbose_name="Nome do representante")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso do Representante')
    semestre = models.CharField(max_length=60, choices=SEMESTRES_CHOICES)
    emailrepresentante = models.EmailField(max_length=100, verbose_name="Email do representante")
    def __str__(self):
        return f'{self.nomerepresentante} - {self.curso} - {self.semestre}'