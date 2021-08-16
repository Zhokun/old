from funcoes import *

while True:
    tab = [" "] * 10
    print("Bem Vindo ao Jogo da velha do Darlan!\n")
    p1, p2 = marcador_x_o()
    vez = primeiro_a_jogar()

    print(f"{vez} joga primeiro")

    game_on = True

    while game_on:
        if vez == 'Jogador01':
            tabuleiro(tab)

            posiciona_marcador(tab, proxima_jogada(tab), p1)

            print("Vez do Jogador2 jogar\n")
            vez = 'Jogador02'

            if verifica_vitoria(tab, p1):
                print("Parabéns! Jogador1 venceu a partida")
                tabuleiro(tab)
                game_on = False
        else:
            tabuleiro(tab)
            posiciona_marcador(tab, proxima_jogada(tab), p2)
            print("Vez do Jogador01 jogar\n")
            vez = 'Jogador01'

            if verifica_vitoria(tab, p2):
                print("Parabéns! Jogador2 venceu a partida")
                game_on = False
    if not replay():
        break


