# Exercício 3 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores.

def numeros_divisores():

    numero = int(input('Digite um número inteiro e o programa exibirar todos os seus divisores:'))
    print(f'Divisores de {numero}:')
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
numeros_divisores()
