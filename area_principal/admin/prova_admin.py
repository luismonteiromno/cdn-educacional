from django.contrib import admin


from ..models import Prova


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ['id', 'disciplina', 'turma', 'data']
    
    search_fields = ['disciplina__nome', 'professor__usuario__first_name', 'turma__nome']
    
    list_filter = ['disciplina', 'turma__nome', 'bimestre']
    
    autocomplete_fields = ['disciplina', 'professor', 'turma']
    
    radio_fields = {'bimestre': admin.VERTICAL}
    