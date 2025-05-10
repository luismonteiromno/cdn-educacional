from rest_framework import serializers


from ..models import FrequenciaAluno

from area_principal.serializers import TurmaSerializer, AlunoSerializer, ProfessorSerializer


class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, read_only=True)
    turma = TurmaSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    
    class Meta:
        model = FrequenciaAluno
        fields = '__all__'
        