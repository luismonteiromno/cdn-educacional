from rest_framework import serializers


from ..models import FrequenciaAluno

from area_principal.serializers import TurmaSerializer


class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    alunos = serializers.StringRelatedField(many=True, read_only=True)
    turma = TurmaSerializer(read_only=True)
    professor = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = FrequenciaAluno
        fields = '__all__'
        