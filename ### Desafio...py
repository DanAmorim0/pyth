### Desafio... Jogo de advinhação

### 1. O computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar advinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
 # vamos usar o método Randit para gerar um número aleatório entre 0 e 10
numero_sorteado = random.randint(0, 10)
print("O computador está sorteando um número entre 0 e 10.")
time.sleep(1)
print("O computador está sorteando um número entre 0 e 10..")
time.sleep(1)
print("O computador está sorteando um número entre 0 e 10...")
time.sleep(1)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')

# Jogo de advinhação
acertou = False
palpites = 0
while acertou == False:
    palpite_do_jogador = int(input('Qual é o seu palpite (número de 0 a 10)? '))
    if palpite_do_jogador == numero_sorteado:
        acertou = True
        print('Parabéns! Você acertou!')
    else:
        palpites += 1
        print('Você errou! Tente novamente.')
print(f'Você precisou de {palpites} palpites para acertar.')
