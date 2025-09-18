import random
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
    jogador["forca"] += item["bonus_forca"]
    jogador["defesa"] += item["bonus_defesa"]
    jogador["agilidade"] += item["bonus_agilidade"]
    jogador["magia"] += item["bonus_magia"]
    print(f"{jogador['nome']} usou {item['nome']} e recebeu os bônus!")
    

def fugir(jogador,inimigo):
    if jogador["agilidade"] > inimigo["agilidade"]:
        random_chance = random.randint(1, 100)
        if random_chance <= 85:  # 85% de chance de sucesso
            print(f"{jogador['nome']} conseguiu fugir de {inimigo['nome']}!")
            return True
        else:
            print(f"{jogador['nome']} não conseguiu fugir de {inimigo['nome']}!")
            return False
        
        
    else:
        random_chance = random.randint(1, 100)
        if random_chance <= 60:  # 60% de chance de sucesso
            print(f"{jogador['nome']} conseguiu fugir de {inimigo['nome']}!")
            return True
        else:
            print(f"{jogador['nome']} não conseguiu fugir de {inimigo['nome']}!")
            return False


#    class Item(models.Model):
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



# class Personagem(models.Model):
#     nome = models.CharField(max_length=100)
#     nivel = models.IntegerField(default=1)
#     vida = models.IntegerField(default=40)
#     forca = models.IntegerField(default=5)
#     defesa = models.IntegerField(default=5)
#     velocidade = models.IntegerField(default=10)
#     magia = models.IntegerField(default=5)
    
#     def __str__(self):
#         return self.nome
