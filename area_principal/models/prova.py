from django.db import models


class Prova(models.Model):
    disciplina = models.ForeignKey(
        'area_principal.Disciplina',
        verbose_name='Disciplina',
        on_delete=models.PROTECT
    )
    
    turma = models.ForeignKey(
        'area_principal.Turma',
        verbose_name='Turma',
        on_delete=models.PROTECT
    )
    
    professor = models.ForeignKey(
        'area_principal.Professor',
        verbose_name='Professor',
        on_delete=models.PROTECT
    )
    
    BIMESTRES = (
        ('1° Bimestre', '1° Bimestre'),
        ('2° Bimestre', '2° Bimestre'),
        ('3° Bimestre', '3° Bimestre'),
        ('4° Bimestre', '4° Bimestre')
    )
    
    bimestre = models.CharField(
        'Bimestre',
        max_length=20,
        choices=BIMESTRES,
        blank=True,
        null=True
    )
    
    data = models.DateField(
        'Data de aplicação'
    )
    
    def __str__(self) -> str:
        return f'{self.disciplina} - {self.turma} - {self.data}'
    
    class Meta:
        verbose_name = 'Prova'
        verbose_name_plural = 'Provas'
        