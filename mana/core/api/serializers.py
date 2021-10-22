from rest_framework import serializers
from core.models import Profissional, Startup, AreaAtuacao


class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Mudar para profissional
        model = AreaAtuacao
        fields = '__all__'
