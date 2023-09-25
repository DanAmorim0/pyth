# Exercício 5 - Escreva um programa que encontra quais números são divisíveis por 7 e não são múltiplos de 5, entre 2000 e 3200 (inclusive). Imprima o seu resultado no console em uma única linha separada por vírgulas.

def multiplos_7():
    numeros = []

    for numero in range(2000, 3201):
        if numero % 7 == 0 and numero % 5 != 0:
            numeros.append(numero)

    resultado = ', '.join(map(str, numeros))
    print(resultado)

multiplos_7()