from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import FrequenciaAluno
from ..serializers import FrequenciaAlunoSerializer


class FrequenciaAlunoViewSet(ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = ['turma', 'professor']
    