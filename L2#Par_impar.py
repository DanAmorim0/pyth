# Par ou ímpar:
### Crie um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar se o número é par ou ímpar.
### Bônus: permita que o usuário jogue contra outro usuário humano.

import random

def par_impar():
    numero_maquina = random.randint(1, 10)
    resultado = (numero_maquina % 2 == 0)

    print(f'O computador escolheu o número {numero_maquina}.')

    print('Jogador 1, é a sua vez.')
    jogador1 = input('Digite "par" ou "impar": ').lower()
    
    if jogador1 != "par" and jogador1 != "impar":
        print(input('Jogador 1, escolha uma opção válida: "par" ou "impar":'))
        return
    
    print('Jogador 2, é a sua vez.')
    jogador2 = input('Digite "par" ou "impar": ').lower()
    
    if jogador2 != "par" and jogador2 != "impar":
        print(input('Jogador 2, escolha uma opção válida: "par" ou "impar".'))
        return 
    if (jogador1 == 'par' and resultado) or (jogador1 == 'impar' and not resultado):
        print('Jogador 1 ganhou!')
    elif (jogador2 == 'par' and resultado) or (jogador2 == 'impar' and not resultado):
        print('Jogador 2 ganhou!')
    else:
        print('Empate!')

par_impar()

