from rest_framework import serializers


from ..models import Turma

from .disciplina_serializer import DisciplinaSerializer

class TurmaSerializer(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Turma
        fields = '__all__'
        