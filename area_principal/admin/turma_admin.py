from django.contrib import admin


from ..models import Turma

from .alunos_inline import AlunoInline

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'turno']
    
    search_fields = ['nome']
    
    list_filter = ['turno']
    
    inlines = [AlunoInline]
    