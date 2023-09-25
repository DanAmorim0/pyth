# Exercício 6 - Escreva um aplicativo que solicita ao usuário inserir um número e retorna o seu fatorial.

def fatorial():
    numero = int(input("Digite um número inteiro para saber seu fatorail: "))
    
    if numero < 0:
        print('Não é possivel fatorar números negativos!')
        return
    if numero == 0:
        print('O fatorial de 0 é 1')
        return
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    
    print(f'O fatorial de {numero} é {resultado}')
fatorial()
