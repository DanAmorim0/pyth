# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def palavra_polindromo():
    palavra = input("DIGITE UMA PALAVRA AQUI:")
    if palavra == palavra[::-1]:
        print("A palavra digitada é políndroma!")
    else:
        print('A palavra digitada não é políndroma!')
palavra_polindromo()