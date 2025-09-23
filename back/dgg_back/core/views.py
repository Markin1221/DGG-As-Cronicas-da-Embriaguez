from django.shortcuts import render
from rest_framework import viewsets
from .models import Personagem, Item, Bebida,ataque
from .serializers import CharacterSerializer, ItemSerializer, DrinkSerializer,AttackSerializer
# game/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = CharacterSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = DrinkSerializer

class ataqueViewSet(viewsets.ModelViewSet):
    
    def post(self,request):
        Personagem_id=request.data.get('Personagem_id')
        ataque_id=request.data.get('ataque_id')
        inimigo_id=request.data.get('inimigo_id')
        
        try:
            Personagem = Personagem.objects.get(pk=Personagem_id)
            ataque = ataque.objects.get(pk=ataque_id)
            inimigo = Personagem.objects.get(pk=inimigo_id)
            
        except Personagem.DoesNotExist:
            return Response({'error': 'Personagem not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except ataque.DoesNotExist:
            return Response({'error': 'Attack not found'}, status=status.HTTP_404_NOT_FOUND)
        except inimigo.DoesNotExist:
            return Response({'error': 'Inimigo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        dano = ataque.dano + Personagem.forca - inimigo.defesa
        if dano < 0:
            dano = 0
        
        inimigo.vida -= dano
        if inimigo.vida < 0:
            inimigo.vida = 0
        inimigo.save() # aqui eu to pensando em depois mudar tipo, puxa o inimigo,clona e joga num banco da batalha,
                        #ai se puxar dnv o mesmo inimigo ele n ta sem vida
        
        return Response({
            'ataque': ataque.nome,
            'dano': dano,
            'inimigo_vida_restante': inimigo.vida
        }, status=status.HTTP_200_OK)