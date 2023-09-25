# Exerício 2 - Escreva um programa que solicita dois números inteirtos (sendo o primeiro o limite inferior e o segundo o limite superior) e exibe todos os números pares entre esses limites.

def numeros_pares():
    print('Digite dois numeros inteiro, o primeiro será o limite inferior e o segundo o limite superior.')
    primeiro_numero = int(input('Digite o primeiro número: '))
    segundo_numero = int(input('Digite o segundo número: '))
    for numero in range(primeiro_numero, segundo_numero):
        if numero % 2 == 0:
            print(numero)
numeros_pares()