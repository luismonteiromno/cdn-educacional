from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Turma
from ..serializers import TurmaSerializer


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class TurmaFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    turno = filters.CharFilter(field_name='turno', lookup_expr='exact')
    disciplinas__in = NumberInFilter(
        field_name='disciplinas__id',
        lookup_expr='in'
    )

    class Meta:
        model = Turma
        fields = ['nome', 'turno', 'disciplinas__in']


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    
    filterset_class = TurmaFilter
