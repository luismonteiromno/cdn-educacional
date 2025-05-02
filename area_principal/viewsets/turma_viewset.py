from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import Turma
from ..serializers import TurmaSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]
    