from rest_framework import serializers


from ..models import Prova

from .turma_serializer import TurmaSerializer
from .disciplina_serializer import DisciplinaSerializer
from .professor_serializer import ProfessorSerializer

class ProvaSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    disciplina = DisciplinaSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    
    class Meta:
        model = Prova
        fields = '__all__'
        