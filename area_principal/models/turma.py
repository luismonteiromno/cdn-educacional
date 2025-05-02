from django.db import models

class Turma(models.Model):
    nome = models.CharField(
        'Nome da turma',
        max_length=100
    )
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        