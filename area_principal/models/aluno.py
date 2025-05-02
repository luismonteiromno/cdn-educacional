from django.db import models


class Aluno(models.Model):
    usuario = models.OneToOneField(
        'area_principal.Usuario',
        verbose_name='Aluno',
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'Aluno'}
    )
    
    matricula = models.CharField(
        'Matricula',
        max_length=20,
        unique=True
    )
    
    data_nascimento = models.DateField(
        'Data de nascimento'
    )
    
    endereco = models.CharField(
        'Endereço',
        max_length=200
    )
    
    turma = models.ForeignKey(
        'area_principal.Turma',
        verbose_name='Turma',
        on_delete=models.PROTECT
    )
    
    responsaveis = models.ManyToManyField(
        'area_principal.Responsavel',
        verbose_name='Responsáveis',
    )
    
    def __str__(self) -> str:
        return self.usuario.get_full_name()
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        