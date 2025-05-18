from rest_framework import serializers

from ..models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    turmas = serializers.StringRelatedField(many=True, read_only=True)
    disciplinas = serializers.StringRelatedField(many=True, read_only=True)
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'
