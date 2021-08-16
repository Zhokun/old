import random


def tabuleiro(tab):

    print(f"  {tab[1]} |  {tab[2]}  |  {tab[3]}  \n"
          f"---------------\n"
          f"  {tab[4]} |  {tab[5]}  |  {tab[6]}  \n"
          f"---------------\n"
          f"  {tab[7]} |  {tab[8]}  |  {tab[9]}  \n"
          )


def posiciona_marcador(tab, posi, marcador):
    tab[posi] = marcador


def verifica_vitoria(tab, marcador):

    return ((tab[1] == marcador and tab[2] == marcador and tab[3] == marcador) or  # topo
        (tab[4] == marcador and tab[5] == marcador and tab[6] == marcador) or  # meio
        (tab[7] == marcador and tab[8] == marcador and tab[9] == marcador) or  # baixo
        (tab[1] == marcador and tab[4] == marcador and tab[7] == marcador) or  # esquerda
        (tab[2] == marcador and tab[5] == marcador and tab[8] == marcador) or  # meio vertical
        (tab[3] == marcador and tab[6] == marcador and tab[9] == marcador) or  # direita
        (tab[1] == marcador and tab[5] == marcador and tab[9] == marcador) or  # diagonal 1
        (tab[7] == marcador and tab[5] == marcador and tab[3] == marcador))  # diagonal 2


def marcador_x_o():
    marcador = ''

    while not (marcador == "X" or marcador == "O"):
        marcador = input("Primeiro jogador será X ou O? ").upper()
        if marcador == "X":
            return "X", "O"
        elif marcador == "O":
            return "O", "X"


def primeiro_a_jogar():
    if random.randint(0, 1) == 1:
        return 'Jogador01'
    else:
        return 'Jogador02'


def posicao_disponivel(tab, posi):
    if tab[posi] == ' ':
        return tab[posi] == ' '
    else:
        return print("\nPosição não disponível\n")


def tabuleiro_cheio(tab):
    for posicao in range(1, 10):
        if posicao_disponivel(tab, posicao):
            return False
    return True


def proxima_jogada(tab):
    posicao = 0

    while posicao not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not posicao_disponivel(tab, posicao):
        posicao = int(input("Onde deseja jogar?\n"))

    return posicao


def replay():
    x = ''

    while x != "S" or x != "N":
        x = input("Deseja jogar novamente? <S> ou <N>").upper()
        if x == 'S':
            return True
        elif x == "N":
            print("Jogo encerrado")
            return False
        else:
            print("Opção inválida")
