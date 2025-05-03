from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import Prova
from ..serializers import ProvaSerializer


class ProvaViewSet(ModelViewSet):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = ['professor', 'disciplina']
    