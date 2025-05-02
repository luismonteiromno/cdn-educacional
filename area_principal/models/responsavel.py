from django.db import models


class Responsavel(models.Model):
    responsavel = models.OneToOneField(
        'area_principal.Usuario',
        verbose_name='Responsável',
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'Responsavel'}
    )
    
    def __str__(self) -> str:
        return self.responsavel.get_full_name()
    
    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        