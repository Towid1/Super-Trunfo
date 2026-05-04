#FUNÇÃO DOS TURNOS DE JOGADORES REAIS
def turno(vez,carta):
        input(f"Vez do jogador {vez} Pressione enter para continuar!")
        print("Sua carta atual:",carta)
        print("Qual atributo você quer comparar?")
        while True:
            atributo = int(input("Número da dex (1), IV total (2) ou Peso (3): "))
            if atributo == 1 or atributo == 2 or atributo == 3:
                return atributo
            else:
                print("Valor inválido! Tente novamente.")

#FUNÇÃO PARA NOMEAR O ATRIBUTO ESCOLHIDO
def nome_atributo(n):
    if n == 1:
        return "Número da Dex"
    elif n == 2:
        return "IV total"
    elif n == 3:
        return "Peso"                