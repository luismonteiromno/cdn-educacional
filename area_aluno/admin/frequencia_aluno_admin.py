from django.contrib import admin

from ..models import FrequenciaAluno


@admin.register(FrequenciaAluno)
class FrequenciaAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'turma', 'professor', 'data']
    
    search_fields = ['aluno__usuario__first_name', 'turma__nome', 'professor__usuario__first_name', 'professor__usuario__username']
    
    list_filter = ['turma__nome', 'professor__usuario__username']
    
    autocomplete_fields = ['alunos', 'turma', 'professor']
    
    readonly_fields = ['data']
    