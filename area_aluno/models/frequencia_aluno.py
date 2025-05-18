from django.db import models


class FrequenciaAluno(models.Model):
    alunos = models.ManyToManyField(
        'area_principal.Aluno',
        verbose_name='Alunos',
    )
    
    alunos_faltas_abonadas = models.ManyToManyField(
        'area_principal.Aluno',
        verbose_name='Alunos que justificaram a falta',
        related_name='alunos_faltas_abonadas',
        blank=True
    )

    turma = models.ForeignKey(
        'area_principal.Turma',
        verbose_name='Turma',
        on_delete=models.CASCADE
    )
    
    data = models.DateField(
        'Data',
        auto_now_add=True
    )
    
    professor = models.ForeignKey(
        'area_principal.Professor',
        verbose_name='Professor',
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f'{self.professor} - {self.turma} - {self.data}'
    
    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'
        
