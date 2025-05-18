from .aluno_viewset import AlunoViewSet
from .disciplina_viewset import DisciplinaViewSet
from .nota_viewset import NotaViewSet
from .professor_viewset import ProfessorViewSet
from .prova_viewset import ProvaViewSet
from .responsavel_viewset import ResponsavelViewSet
from .turma_viewset import TurmaViewSet
from .usuario_viewset import UsuarioViewSet

__all__ = [
    AlunoViewSet,
    DisciplinaViewSet,
    NotaViewSet,
    ProfessorViewSet,
    ProvaViewSet,
    ResponsavelViewSet,
    TurmaViewSet,
    UsuarioViewSet,
]
