from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from ..models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'matricula']

    fieldsets = [
        [
            'Informações principais',
            {
                'fields': [
                    'usuario',
                    'matricula',
                    'data_nascimento',
                    'endereco',
                    'aprovado',
                ]
            },
        ],
        [
            'Informações escolares',
            {
                'fields': [
                    'turma',
                    'porcentagem_frequencia',
                    'responsaveis',
                ]
            },
        ],
    ]

    list_filter = [AutocompleteFilterFactory('Pesquisar por turma', 'turma')]

    search_fields = ['usuario__first_name', 'usuario__last_name', 'matricula']

    filter_horizontal = ['responsaveis']

    autocomplete_fields = ['usuario', 'turma']

    readonly_fields = ['matricula', 'porcentagem_frequencia', 'aprovado']
