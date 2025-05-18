from django.contrib import admin

from ..models import Responsavel


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['id', 'responsavel']

    fieldsets = [
        [
            'Informações pessoais para contato',
            {'fields': ['responsavel', 'parentesco', 'cpf', 'telefone']},
        ]
    ]

    search_fields = ['responsavel']

    autocomplete_fields = ['responsavel']
