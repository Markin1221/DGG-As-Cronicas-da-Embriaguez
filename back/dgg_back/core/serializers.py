from rest_framework import serializers
from .models import Personagem, Item, Bebida

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'