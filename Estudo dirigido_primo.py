# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.
def primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

numero = int(input('Digite um número inteiro e digo se ele é primo ou nem: '))
if primo(numero):
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um número primo')
