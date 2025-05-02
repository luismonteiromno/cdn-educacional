from django.contrib import admin

from ..models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'matricula']

    search_fields = ['usuario', 'matricula']
    
    filter_horizontal = ['responsaveis']
    
    autocomplete_fields = ['usuario', 'turma']