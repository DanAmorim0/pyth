# Exercício 1 -  Escreva um programa que deve listar no console todos os números divisíveis por 5 entre 1 e 100 (inclusive).
def dividiseis():
    for numero in range (1, 100):
        if numero % 5 == 0:
            print(numero)
dividiseis()