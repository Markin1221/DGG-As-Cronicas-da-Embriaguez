from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)
    vida = models.IntegerField(default=40)
    forca = models.IntegerField(default=5)
    defesa = models.IntegerField(default=5)
    velocidade = models.IntegerField(default=10)
    magia = models.IntegerField(default=5)
    
    def __str__(self):
        return self.nome
    
class Item(models.Model):
    nome = models.CharField(max_length=100)
    bonus_forca = models.IntegerField(default=0)
    bonus_defesa = models.IntegerField(default=0)
    bonus_agilidade = models.IntegerField(default=0)
    bonus_magia = models.IntegerField(default=0)
    bonus_vida = models.IntegerField(default=0)
    preco = models.IntegerField(default=0)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
# Esse aqui eu to pensando se ele vai dar buff e debuff ou vai mudar algo na jogabilidade
# talvez eu faça as bebidas mudar o estilo de luta, tipo vinho é corpo a corpo e vodka a magica por exemoplo
class Bebida(models.Model):
    nome = models.CharField(max_length=100)
    efeito = models.TextField()  # Ex: "Aumenta força mas diminui defesa"
    bonus_vida = models.IntegerField(default=0)
    bonus_forca = models.IntegerField(default=0)
    malus_defesa = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class ataque(models.Model):
    nome = models.CharField(max_length=100)
    dano = models.IntegerField(default=0)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome