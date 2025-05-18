from rest_framework import serializers

from ..models import Aluno
from .turma_serializer import TurmaSerializer


class AlunoSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    porcentagem_frequencia = serializers.ReadOnlyField()

    class Meta:
        model = Aluno
        fields = '__all__'
