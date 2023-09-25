# Exercício 16 - Considere a seguinte lista: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ----> e escreva um programa que imprime todos os elementos da lista que são menores que 5.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def impressora():  
    lista2 = []
    lista3 = []
    for i in lista:
        if i <= 5:
            lista2.append(i)
    print(lista2)
    
    numero = int(input("Digite um número até 100: "))
    for i in lista:
        if numero >= i:
            lista3.append(i)
    print(lista3)
impressora()

"""Extras:

Em vez de imprimir os elementos um por um, crie uma nova lista que contenha todos os elementos menores que 5 dessa lista e imprima essa nova lista.
Escreva isso em uma única linha de Python.
Peça ao usuário um número e retorne uma lista que contenha apenas elementos da lista original "a" que sejam menores do que o número fornecido pelo usuário."""