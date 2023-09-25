# Exercício 7 - Escreva um programa em que o usuário insere um número inteiro positivo n e o programa retorna a soma de todos os números inteiros positivos entre 1 e n.

def nrm_n():

    numero = int(input('Digite um número inteiro positivo e o programa vai retornar a soma de todos os numeros entre 1 e o que vc escolheu: '))
    soma = 0
    for i in range(1,numero):
        soma += i
    print(f'A soma de todos os números entre 1 e {numero} é {soma}')
nrm_n()
