from rest_framework import serializers
from .models import Personagem, Item, Bebida,ataque

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = ['id', 'name', 'health', 'attacks']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'
        

class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ataque
        fields = ['id', 'name', 'power', 'mana_cost', 'description']

