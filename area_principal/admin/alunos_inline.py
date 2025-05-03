from django.contrib import admin


from ..models import Aluno


class AlunoInline(admin.TabularInline):
    model = Aluno
    extra = 1
    verbose_name = 'Aluno'
    verbose_name_plural = 'Alunos da turma'
    
    autocomplete_fields = ['responsaveis']
    
    readonly_fields = ['matricula', 'data_nascimento']
    