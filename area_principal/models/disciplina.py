from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(
        'Nome da disciplina',
        max_length=100
    )
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        