from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class SubstituicaoAula(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_solicitadas', verbose_name='Solicitante')
    data_hora_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora da Solicitação')
    data_hora_aula_substituida = models.DateTimeField(verbose_name='Data e Hora da Aula a ser Substituída')
    substituto_nome = models.CharField(max_length=255, verbose_name='Nome do Substituto', null=True, blank=True)
    turma_afetada = models.CharField(max_length=50, verbose_name='Turma Afetada')

    def __str__(self):
        return f'{self.solicitante.username} - {self.data_hora_solicitacao}'

    class Meta:
        verbose_name = 'Substituição de Aula'
        verbose_name_plural = 'Substituições de Aula'