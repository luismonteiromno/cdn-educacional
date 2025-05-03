from django.contrib import admin


from ..models import Nota


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'professor', 'prova_feita', 'nota']
    
    search_fields = ['aluno__usuario__first_name', 'professor__usuario__first_name', 'prova_feita__disciplina__nome', 'prova_feita__turma__nome']
    
    list_filter = ['professor', 'prova_feita']
    
    autocomplete_fields = ['aluno', 'professor', 'prova_feita']
    