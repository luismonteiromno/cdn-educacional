from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    TIPOS_USUARIOS = (
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
        ('Responsavel', 'Responsavel'),
        ('Coordenador', 'Coordenador'),
        ('Administrador', 'Administrador')
    )
    
    tipo = models.CharField(
        'Tipo do usuário',
        max_length=20,
        choices=TIPOS_USUARIOS
    )
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        