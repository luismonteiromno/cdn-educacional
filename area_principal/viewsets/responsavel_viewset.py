from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import Responsavel
from ..serializers import ResponsavelSerializer


class ResponsavelViewSet(ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    permission_classes = [IsAuthenticated]
    