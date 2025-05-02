from rest_framework import serializers

from .turma_serializer import TurmaSerializer

from ..models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    
    class Meta:
        model = Aluno
        fields = '__all__'
        