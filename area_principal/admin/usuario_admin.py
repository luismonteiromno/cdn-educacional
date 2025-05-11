from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ..models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    model = Usuario

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'tipo',
        'is_active',
        'is_staff',
    )
    list_filter = ('tipo', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('id',)

    fieldsets = (
        ('Dados de Login', {'fields': ('username', 'password')}),
        (
            'Informações Pessoais',
            {'fields': ('first_name', 'last_name', 'email', 'tipo')},
        ),
        (
            'Permissões',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'tipo',
                    'is_staff',
                    'is_active',
                ),
            },
        ),
    )

    radio_fields = {'tipo': admin.VERTICAL}
