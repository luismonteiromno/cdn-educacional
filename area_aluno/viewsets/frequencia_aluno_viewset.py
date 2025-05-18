from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import FrequenciaAluno
from ..serializers import FrequenciaAlunoSerializer


class FrequenciaAlunoViewSet(ModelViewSet):
    queryset = FrequenciaAluno.objects.all().order_by('-id')
    serializer_class = FrequenciaAlunoSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['turma', 'professor']

    @action(
        detail=False, methods=['POST'], permission_classes=[IsAuthenticated]
    )
    def lancar_frequencia(self, request):
        usuario = request.user
        data = request.data
        turma = data.get('turma')
        alunos = data.get('alunos', [])
        alunos_faltas_abonadas = data.get('faltas_abonadas', [])

        if usuario.tipo != 'Professor':
            return Response(
                {'Error': 'Apenas professores podem lançar frequência'},
                status=403,
            )

        if not turma:
            return Response(
                {'Error': 'A turma deve ser informada!'}, status=400
            )

        if not alunos:
            return Response(
                {'Error': 'O campo de alunos não pode ser vazio!'}, status=400
            )

        frequencia = FrequenciaAluno.objects.create(
            turma_id=turma, professor=usuario.professor
        )
        frequencia.alunos.add(*alunos)
        frequencia.alunos_faltas_abonadas.add(*alunos_faltas_abonadas)

        return Response(
            {
                'message': 'Frequência lançada com sucesso',
                'data': FrequenciaAlunoSerializer(frequencia).data,
            },
            status=200,
        )
