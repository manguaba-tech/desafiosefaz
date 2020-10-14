from rest_framework import serializers
from app.processamento.models import Classificacao


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = '__all__'
