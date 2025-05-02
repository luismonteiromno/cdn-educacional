from django.contrib import admin


from ..models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'turno']
    
    search_fields = ['nome']
    
    list_filter = ['turno']
    