# JOGADOR 1
def turno(vez,carta):
        input(f"Vez do jogador {vez} Pressione enter para continuar!")
        print("Sua carta atual:",carta)
        print("Qual atributo você quer comparar?")
        while True:
            atributo = int(input("Número da dex(1), IV total(2) ou Peso(3): "))
            if atributo == 1 or atributo == 2 or atributo == 3:
                return atributo
            else:
                print("Valor inválido! Tente novamente.")

def teste_de_vitória(p1,p2,baralho):
     if len(p1) == len(baralho):
          return "Jogador 1"
     elif len(p2) == len(baralho):
          return "Jogador 2"
 
    