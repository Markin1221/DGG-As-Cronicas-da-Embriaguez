from django.shortcuts import render
from rest_framework import viewsets
from .models import Personagem, Item, Bebida
from .serializers import PersonagemSerializer, ItemSerializer, BebidaSerializer

class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
