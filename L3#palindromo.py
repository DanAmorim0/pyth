# Exercício 17 - Escreva um programa que solicita ao usuário inserir uma palavra e retorna se a palavra é um palíndromo ou não.

def pali():
    palavra = input('Digite uma palavra pra ver se ela é palindromo ou não:').lower()
    palindromo =[]
    if palavra == palavra[::-1]:
        palindromo.append(palavra[::-1])
        print(f'A palavra: {palavra}, é palindromo!')
        print(palindromo)
    else:
        palindromo.append(palavra[::-1])
        print(f'A palavra: {palavra}, não é palindromo!')
        print(palindromo)
    
pali()