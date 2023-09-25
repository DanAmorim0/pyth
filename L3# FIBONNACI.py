# Exercício 15 - Crie um programa em que o usuário deve responder no terminal quantos números de Fibonacci ele deseja ver. Em seguida, o programa deve imprimir os números de Fibonacci na tela em uma lista separada por vírgulas.

def fibonaci():
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append (a)
        a, b = b, a + b
    return lista

try:
    n = int(input('Quantos números de Fibonnaci você quer ver? '))
    if n < 1:
        print('Digite um número positivo maior ou igual a 1.')
    else:
        resultado = fibonaci()
        print("Números de Fibonnaci: ", resultado)
except ValueError:
    print('Digite um número inteiro válido!')


