from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from ..models import FrequenciaAluno


@admin.register(FrequenciaAluno)
class FrequenciaAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'turma', 'professor', 'data']

    search_fields = [
        'aluno__usuario__first_name',
        'turma__nome',
        'professor__usuario__first_name',
        'professor__usuario__username',
    ]

    list_filter = [
        AutocompleteFilterFactory('Pesquisar por turma', 'turma'),
        AutocompleteFilterFactory('Pesquisar por professor', 'professor'),
    ]

    autocomplete_fields = ['alunos', 'turma', 'professor']

    readonly_fields = ['data']
