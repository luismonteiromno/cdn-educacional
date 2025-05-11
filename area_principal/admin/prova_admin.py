from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from ..models import Prova


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ['id', 'disciplina', 'turma', 'data']

    search_fields = [
        'disciplina__nome',
        'professor__usuario__first_name',
        'turma__nome',
    ]

    list_filter = [
        AutocompleteFilterFactory('Pesquisar por disciplina', 'disciplina'),
        AutocompleteFilterFactory('Pesquisar por turma', 'turma'),
        'bimestre',
    ]

    autocomplete_fields = ['disciplina', 'professor', 'turma']

    radio_fields = {'bimestre': admin.VERTICAL}
