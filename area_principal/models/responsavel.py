from django.db import models


class Responsavel(models.Model):
    responsavel = models.OneToOneField(
        'area_principal.Usuario',
        verbose_name='Responsável',
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'Responsavel'}
    )
    
    PARENTESCO = (
        ('Pai', 'Pai'),
        ('Mãe', 'Mãe'),
        ('Responsável', 'Responsável')
    )
    
    parentesco = models.CharField(
        'Parentesco',
        choices=PARENTESCO,
        blank=True,
        null=True
    )
    
    cpf = models.CharField(
        'CPF',
        max_length=14,
        unique=True,
        help_text='Ex: 123.456.789-10',
        blank=True,
        null=True
    )
    
    telefone = models.CharField(
        'Telefone',
        max_length=15,
        blank=True,
        null=True
    )
    
    def __str__(self) -> str:
        return self.responsavel.username
    
    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        