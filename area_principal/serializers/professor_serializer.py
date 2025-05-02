from rest_framework import serializers


from ..models import Professor

from .turma_serializer import TurmaSerializer
from .disciplina_serializer import DisciplinaSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    turmas = TurmaSerializer(many=True, read_only=True)
    disciplinas = DisciplinaSerializer(many=True, read_only=True)
    usuario = serializers.SerializerMethodField(read_only=True)
    
    def get_usuario(self, obj):
        return obj.usuario.username
    
    class Meta:
        model = Professor
        fields = '__all__'
        