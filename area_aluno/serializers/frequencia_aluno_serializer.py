from rest_framework import serializers

from area_principal.serializers import TurmaSerializer

from ..models import FrequenciaAluno


class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    alunos = serializers.StringRelatedField(many=True, read_only=True)
    turma = serializers.StringRelatedField(read_only=True)
    professor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FrequenciaAluno
        fields = '__all__'
