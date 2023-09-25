# Exercício 10 - Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna um dicionário que contém (i, i*i) para cada número inteiro positivo i menor ou igual a n. Use o dicionário para imprimir o quadrado de cada número inteiro positivo menor ou igual a n.

def nrm_inteiro(n):
    quadrados = {}
    for i in range(1, n + 1):
        quadrados[i] = i * i
    return quadrados

def nrm_dic():
    numero = int(input('Insira um número inteiro positivo: '))

    if numero <= 0:
        print('Insira um número inteiro positivo!!')
    else:
        resultado = nrm_inteiro(numero)

        for chave, valor in resultado.items():
            print(f'O quadrado de {chave} é {valor}')

nrm_dic()