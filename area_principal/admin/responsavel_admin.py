from django.contrib import admin

from ..models import Responsavel


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['id', 'responsavel']

    search_fields = ['responsavel']

    autocomplete_fields = ['responsavel']
