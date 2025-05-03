from django.db import models


class Nota(models.Model):
    aluno = models.ForeignKey(
        'area_principal.Aluno',
        verbose_name='Aluno',
        on_delete=models.PROTECT
    )
    
    professor = models.ForeignKey(
        'area_principal.Professor',
        verbose_name='Professor',
        on_delete=models.PROTECT
    )
    
    prova_feita = models.ForeignKey(
        'area_principal.Prova',
        verbose_name='Prova feita pelo aluno',
        on_delete=models.PROTECT
    )
    
    nota = models.FloatField(
        'Nota',
        max_length=10
    )
    
    def __str__(self) -> str:
        return f'{self.aluno} - {self.prova_feita} - {self.nota}'
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        