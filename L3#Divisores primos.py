# Exercício 4 - Escreva um programa que solicita um número inteiro e exibe todos os seus divisores primos.

def divisores_primos():

    numero = int(input('Digite um número inteiro:'))
    print(f'Divisores primos de {numero}:')
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    for divisor in divisores:
        if primo(divisor):
            print(divisor)

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

divisores_primos()
