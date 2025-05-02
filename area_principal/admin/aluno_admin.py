from django.contrib import admin

from ..models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'matricula']

    search_fields = ['usuario__first_name', 'usuario__last_name', 'matricula']
    
    filter_horizontal = ['responsaveis']
    
    autocomplete_fields = ['usuario', 'turma']
    
    readonly_fields = ['matricula']
    