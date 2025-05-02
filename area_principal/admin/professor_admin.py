from django.contrib import admin

from ..models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario']
    
    search_fields = ['usuario']
    
    autocomplete_fields = ['usuario', 'disciplinas', 'turmas']
    