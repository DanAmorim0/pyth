# Jogo da Velha:
### Crie um jogo da velha para dois jogadores que permite aos usuários inserir o local onde desejam inserir seu símbolo (X ou O) e mantenha uma contagem das vitórias de cada jogador.
### Bônus: permita que o usuário jogue contra o computador.

import random

vitorias_p1 = 0
vitorias_p2 = 0

tabuleiro = [" " for _ in range(9)]

def exibir_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vitoria(simbolo):
    return ((tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == simbolo) or
            (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == simbolo) or
            (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == simbolo) or
            (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == simbolo) or
            (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo) or
            (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo) or
            (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == simbolo) or
            (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == simbolo))

def jogar_contra_computador():
    global vitorias_p1
    global vitorias_p2
    
    jogador_atual = "X"
    computador = "O"
    
    while True:
        exibir_tabuleiro()
        print(f"Vitórias do Jogador 1: {vitorias_p1}")
        print(f"Vitórias do Computador: {vitorias_p2}")
        
        if jogador_atual == "X":
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[jogada] == " ":
                tabuleiro[jogada] = jogador_atual
            else:
                print("Posição ocupada. Tente novamente.")
                continue
        else:
            jogadas_disponiveis = [i for i, valor in enumerate(tabuleiro) if valor == " "]
            jogada = random.choice(jogadas_disponiveis)
            tabuleiro[jogada] = computador
        
        if verificar_vitoria(jogador_atual):
            exibir_tabuleiro()
            if jogador_atual == "X":
                print(f"Parabéns, Jogador {jogador_atual}! Você venceu!")
                vitorias_p1 += 1
            else:
                print("O Computador venceu!")
                vitorias_p2 += 1
            break
        
        if " " not in tabuleiro:
            exibir_tabuleiro()
            print("Empate!")
            break
        
        jogador_atual, computador = computador, jogador_atual

def jogo_da_velha():
    global vitorias_p1
    global vitorias_p2
    
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro()
        print(f"Vitórias do Jogador 1: {vitorias_p1}")
        print(f"Vitórias do Jogador 2: {vitorias_p2}")
        
        jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
        
        if tabuleiro[jogada] == " ":
            tabuleiro[jogada] = jogador_atual
        else:
            print("Posição ocupada. Tente novamente.")
            continue
        
        if verificar_vitoria(jogador_atual):
            exibir_tabuleiro()
            print(f"Parabéns, Jogador {jogador_atual}! Você venceu!")
            if jogador_atual == "X":
                vitorias_p1 += 1
            else:
                vitorias_p2 += 1
            break
        
        if " " not in tabuleiro:
            exibir_tabuleiro()
            print("Empate!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

while True:
    tabuleiro = [" " for _ in range(9)]
    print("Escolha o modo de jogo:")
    print("1. Dois Jogadores")
    print("2. Jogar contra o Computador")
    modo_jogo = input("Digite o número correspondente ao modo de jogo: ")
    
    if modo_jogo == "1":
        jogo_da_velha()
    elif modo_jogo == "2":
        jogar_contra_computador()
    
