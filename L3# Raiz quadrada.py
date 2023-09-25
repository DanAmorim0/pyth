# Exercício 13 - Crie um programa que entrega a raiz quadrada de um número inteiro positivo n com uma precisão de 0.001.

def raiz_quadrada():
    numero = int(input( 'Digite um número inteiro positivo:'))
    raiz = numero **0.5
    print(f'A raiz quadrada de {numero} é: {raiz:.2f}')

raiz_quadrada()