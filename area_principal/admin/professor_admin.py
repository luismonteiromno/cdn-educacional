from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from ..models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario']
    
    fieldsets = [
        [
            'Informações escolares',
            {
                'fields': [
                    'usuario',
                    'disciplinas',
                    'turmas'
                ]
            }
        ],
        [
            'Informações pessoais',
            {
                'fields': [
                    'salario',
                    'concursado',
                ]
            }
        ]
    ]

    search_fields = ['usuario']

    autocomplete_fields = ['usuario', 'disciplinas', 'turmas']

    list_filter = [
        'disciplinas',
        AutocompleteFilterFactory('Pesquisar por turma', 'turmas'),
    ]
