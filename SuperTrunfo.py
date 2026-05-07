#SuperTrunfo
import random

def turno(vez,carta):
        input(f"\nVez do jogador {vez} Pressione enter para continuar!")
        print(f"\nSua carta atual:\nNome: {carta[0]}\n(1)Dex: {carta[1]}\n(2)IV: {carta[2]}\n(3)Peso: {carta[3]}")
        print("\nQual atributo você quer comparar?")
        while True:
            atributo = int(input("(1)Número da dex, (2)IV total ou (3)Peso: "))
            if atributo == 1 or atributo == 2 or atributo == 3:
                return atributo
            else:
                print("Valor inválido! Tente novamente.")

def nome_atributo(n):
    if n == 1:
        return "Número da Dex"
    elif n == 2:
        return "IV total"
    elif n == 3:
        return "Peso"

def teste_de_vitória(p1,p2,baralho):
     if len(p1) == len(baralho):
          return "Jogador 1"
     elif len(p2) == len(baralho):
          return "Jogador 2"

while True:
    n_jogadores = str(input("Número de jogadores(1 ou 2): "))
    if n_jogadores == "1" or n_jogadores == "2":
        break
    else:
        print("Valor inválido! Tente novamente.")

#   ["Nome",DEX,IVtotal,Peso]
baralho = [
    ["Mudkip",258,310,7.6],
    ["Basculegion",902,530,110],
    ["Shinx",403,263,9.5],
    ["Regice",378,580,175],
    ["Algomon",1022,590,162.5],
    ["Purrloin",509,281,10.1],
    ["Drifloon",425,348,1.2],
    ["Pangoro",675,495,136],
    ["Amoonguss",591,464,10.5],
    ["Mudbray",749,385,110],
    ["Clodsire",980,430,223],
    ["Magcargo",219,430,55],
    ["Riolu",447,285,20.2],
    ["Kyurem",646,660,325],
    ["Kyogre",382,670,352],
    ["Zeraora",807,600,44.5],
    ["Yvetal",717,680,203],
    ["Mewtwo",150,680,122],
    ["Lugia",249,680,216],
    ["Arceus",493,720,320],
    ["Rayquaza",384,680,206.5],
    ["Venipede",543,260,5.3],
    ["Dragonite",149,600,210],
    ["Machop",66, 305, 19.5],
    ["Wailmer",320,400,130],
    ["Groundon",383,670,352],
    ["Darkrai",491,600,50.5],
    ["Scraggy",559,348,11.8],
    ["Annihilape",979,535,56],
    ["Falinks",870,470,62.0],
    ["Zoroark",571,510,81.1],
    ["Druddigon",621,485,139]
]
random.shuffle(baralho)

jogador_1 = baralho[:len(baralho)//2]
jogador_2 = baralho[len(baralho)//2:len(baralho)]
monte_espera = []
vez = 1
rodadas = 0


while len(jogador_1) != 0 and len(jogador_2) != 0:
    rodadas += 1
    carta1 = jogador_1.pop(0)
    carta2 = jogador_2.pop(0)

# SINGLEPLAYER
    if n_jogadores == "1":

    # JOGADOR 1 (Humano)
        if vez == 1:
            atributo = turno(1,carta1)
            vez = 2

    # JOGADOR 2 (Máquina)
        elif vez == 2:
            input(f"\nVez do jogador {vez} (CPU) Pressione enter para continuar!")
            atributo = carta2.index(max(carta2[1:]))
            vez = 1

# MULTIPLAYER
    elif n_jogadores == "2":

    # JOGADOR 1
        if vez == 1:
            atributo = turno(1,carta1)
            vez = 2

    # JOGADOR 2
        elif vez == 2:
            atributo = turno(2,carta2)
            vez = 1

# DISPUTA DA RODADA
    if carta1[atributo] > carta2[atributo]:
        jogador_1 += monte_espera + [carta1] + [carta2]
        monte_espera = []
        print(f"\nO {nome_atributo(atributo)} de {carta1[0]} ({carta1[atributo]}) é maior do que {carta2[0]} ({carta2[atributo]})")
        print(f"Jogador 1 ganhou a rodada! E esta com {len(jogador_1)} cartas de {len(baralho)}.")
    elif carta2[atributo] > carta1[atributo]:
        jogador_2 += monte_espera + [carta2] + [carta1]
        monte_espera = []
        print(f"\nO {nome_atributo(atributo)} de {carta2[0]} ({carta2[atributo]}) é maior do que {carta1[0]} ({carta1[atributo]})")
        print(f"Jogador 2 ganhou a rodada! E esta com {len(jogador_2)} cartas de {len(baralho)}.")
    else:
        monte_espera += [carta1] + [carta2]
        print(f"\nO {nome_atributo(atributo)} de {carta1[0]} e {carta2[0]} são iguais ({carta1[atributo]})")
        print(f"Empate! Monte de espera: {monte_espera}")

print(f"\n{teste_de_vitória(jogador_1,jogador_2,baralho)} venceu! Em {rodadas} rodadas!")