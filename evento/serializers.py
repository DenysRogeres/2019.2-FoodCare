from rest_framework import serializers
from .models import Evento, Alimento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'


class AlimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alimento
        fields = '__all__'

