from rest_framework import serializers


from ..models import Nota

from .aluno_serializer import AlunoSerializer
from .professor_serializer import ProfessorSerializer
from .prova_serializer import ProvaSerializer


class NotaSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    prova_feita = ProvaSerializer(read_only=True)
    
    class Meta:
        model = Nota
        fields = '__all__'
        