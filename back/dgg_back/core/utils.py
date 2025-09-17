#--> Função para Atacar 

def atacar(atacante, alvo):
    dano = atacante["ataque"] - alvo["defesa"]
    if dano <= 0:
        dano = 0
    alvo["vida"] -= dano
    print(f"{atacante['nome']} atacou {alvo['nome']} e causou {dano} de dano")

#-->Função para os Itens

def usar_item(jogador,item):
    
    
    jogador["vida"] += item["bonus_vida"]
    
    
#     class Personagem(models.Model):
#     nome = models.CharField(max_length=100)
#     nivel = models.IntegerField(default=1)
#     vida = models.IntegerField(default=40)
#     forca = models.IntegerField(default=5)
#     defesa = models.IntegerField(default=5)
#     velocidade = models.IntegerField(default=10)
#     magia = models.IntegerField(default=5)
    
#     def __str__(self):
#         return self.nome
    
# class Item(models.Model):
#     nome = models.CharField(max_length=100)
#     bonus_forca = models.IntegerField(default=0)
#     bonus_defesa = models.IntegerField(default=0)
#     bonus_agilidade = models.IntegerField(default=0)
#     bonus_magia = models.IntegerField(default=0)
#     bonus_vida = models.IntegerField(default=0)
#     preco = models.IntegerField(default=0)
#     descricao = models.TextField()
    
#     def __str__(self):
#         return self.nome
    