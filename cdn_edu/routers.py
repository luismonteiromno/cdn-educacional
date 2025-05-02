from rest_framework import routers

from area_principal.viewsets import (
    AlunoViewSet,
    DisciplinaViewSet,
    ProfessorViewSet,
    ResponsavelViewSet,
    TurmaViewSet,
    UsuarioViewSet
)

main_router = routers.DefaultRouter()

main_router.register(
    'alunos',
    AlunoViewSet,
    basename='alunos'
)
main_router.register(
    'disciplinas',
    DisciplinaViewSet,
    basename='disciplinas'
)
main_router.register(
    'professores',
    ProfessorViewSet,
    basename='professores'
)
main_router.register(
    'responsavel',
    ResponsavelViewSet,
    basename='responsavel'
)
main_router.register(
    'turmas',
    TurmaViewSet,
    basename='turmas'
)
main_router.register(
    'usuarios',
    UsuarioViewSet,
    basename='usuarios'
)

