# Exercício 14 - Crie um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna se o número é par ou ímpar.

def par_impar():
    numero = float(input('Digite um número inteiro positivo e o programa retorna se é par ou ímpar: '))
    if numero % 2 == 0:
        print(f'O número: {numero} é par')
    elif numero % 2 != 0:
        print(f'O número: {numero} é ímpar')
    else:
        print('Digite um número valido pf.')
            
par_impar()