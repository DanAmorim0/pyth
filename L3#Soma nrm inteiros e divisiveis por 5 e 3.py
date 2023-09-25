# Exercício 8 -Escreva um programa que solicita ao usuário inserir um número inteiro positivo n e o programa retorna a soma de todos os números inteiros positivos entre 1 e n que são divisíveis por 3 ou 5.

def nrm_inteiro():
    numero = int(input('Digite um número inteiro positivo: '))
    soma = 0
    for i in range(1,numero):
        soma += i
        if i % 3 == 0 and i % 5 == 0:
            print(f'Os números divisiveis por 3 e 5 são: {i}')
    print(f'A soma de todos os números entre 1 e {numero} é {soma}')
nrm_inteiro()