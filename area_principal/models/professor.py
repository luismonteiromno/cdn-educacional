from django.db import models

class Professor(models.Model):
    usuario = models.OneToOneField(
        'area_principal.Usuario',
        verbose_name='Professor',
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'Professor'}
    )
    
    disciplinas = models.ManyToManyField(
        'area_principal.Disciplina',
        verbose_name='Disciplinas'
    )
    
    turmas = models.ManyToManyField(
        'area_principal.Turma',
        verbose_name='Turmas'
    )
    
    salario = models.DecimalField(
        'Salário',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    concursado = models.BooleanField(
        'Concursado',
        default=False
    )
    
    def __str__(self) -> str:
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        