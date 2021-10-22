from rest_framework import viewsets
from rest_framework import permissions
from core.api.serializers import ProfissionalSerializer
from core.models import Profissional, AreaAtuacao


class RecomendacoesViewSet(viewsets.ModelViewSet):

    # Mudar para profissional e montar a query
    queryset = AreaAtuacao.objects.all().order_by('nome')
    serializer_class = ProfissionalSerializer
    permission_classes = [permissions.IsAuthenticated]
