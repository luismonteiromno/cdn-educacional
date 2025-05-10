from django.contrib import admin

from ..models import FrequenciaAluno


@admin.register(FrequenciaAluno)
class FrequenciaAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'turma', 'professor', 'data']
    
    search_fields = ['aluno__usuario__first_name', 'turma__nome', 'professor__usuario__first_name']
    
    list_filter = ['turma']
    
    autocomplete_fields = ['alunos', 'turma', 'professor']
    
    readonly_fields = ['data']
    