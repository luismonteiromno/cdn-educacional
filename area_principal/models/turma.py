from django.db import models

class Turma(models.Model):
    nome = models.CharField(
        'Nome da turma',
        max_length=100
    )
    
    TURNOS = (
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite')
    )
    
    turno = models.CharField(
        'Turno',
        max_length=20,
        choices=TURNOS,
        blank=True,
        null=True
    )
    
    disciplinas = models.ManyToManyField(
        'area_principal.Disciplina',
        verbose_name='Disciplinas da turma',
        blank=True
    )
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.turno}'
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        