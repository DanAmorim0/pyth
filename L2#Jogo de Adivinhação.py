# Jogo de Adivinhação:
###Implemente um jogo simples em que o computador escolhe um número aleatório e o usuário tenta adivinhar o número.
### Bônus: faça o computador informar se o número inserido pelo usuário é maior ou menor que o número escolhido pelo computador.
import random

def jogo_de_adivinhacao():
    nrm_aleatorio = random.randint(1, 10)
    tentativas = 0

    print('Tente adivinhar um número de 1 a 10')

    while True:
        try:
            chute = int(input('Insira seu chute: '))
            tentativas +=1

            if chute == nrm_aleatorio:
                print('Parabens, você acertou')
            elif chute >= nrm_aleatorio:
                print('O número escolhido é maior que o número escolhido pela maquina!')
            elif chute <= nrm_aleatorio:
                print('O número escolhido é menor que o número escolhido pela manquina!')
            else:
                print('Insira somente números entre 1 e 10')
        except ValueError:
            print('Insira somento números e entre 1 e 10')
jogo_de_adivinhacao()                
