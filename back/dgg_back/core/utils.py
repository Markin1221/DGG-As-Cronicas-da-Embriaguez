#--> Função para Atacar 

def atacar(atacante, alvo):
    dano = atacante["ataque"] - alvo["defesa"]
    if dado <= 0
        dano = 0
    alvo["vida"] -= dano
    print(f"{atacante['nome']} atacou {alvo['nome']} e causou {dano} de dano")

#-->Função para os Itens

def usar_item(jogardor,item):
    if item  not in jogador ["itens"] or jogador["itens"][item]<=0
        print("Você não tyem esse item")
        return

    if item == "Agua de coco" 
        cura = 30
        jogar["vida"] += cura
        print(f"{jogador["nome"]} usou uam Agua de coco e curou {cura} de vida")

    elif == "Corotinho"
        aumenta_ataque = 10
        jogador["ataque"] += aumenta_ataque   
        print(f"{jogador["nome"]} usou um corotinho e aumentou seu ataque em {aumenta_ataque}")

    jogador["itens"][item] -= 1   