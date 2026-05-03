#SuperTrunfo
import random

#   ["Nome",DEX,IVtotal,Peso]
baralho = [
    ["Mudkip",258,310,7.6],
    ["Basculegion",902,530,110],
    ["Shinx",403,263,9.5],
    ["Regice",378,580,175],
    ["Iron Boulder",1022,590,162.5],
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
    ["Ground",383,670,352],
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

print(jogador_1,len(jogador_1))
print("-------------------")
print(jogador_2,len(jogador_2))