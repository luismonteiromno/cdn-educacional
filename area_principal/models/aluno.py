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
        unique=True,
        blank=True,
        null=True
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
    
    aprovado = models.BooleanField(
        'Aprovado',
        blank=True,
        null=True
    )
    
    @property
    def gerar_matricula(self):
        import secrets
        import pendulum
        data = pendulum.today()
        
        matricula = f'{data.year}{data.month}{secrets.token_hex(4)}'
        return matricula
    
    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.gerar_matricula
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.usuario.get_full_name()
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        