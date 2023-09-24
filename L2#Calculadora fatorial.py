# Calculadora de Fatorial:
### Crie uma calculadora que permita ao usuário calcular o fatorial de qualquer número.
### Bônus: faça o programa retornar um erro se o usuário inserir um número negativo.

def calculadora_fatorail():
    try:
        numero = int(input('Digite um número inteiro para calcular o fatorial: '))
        if numero < 0:
            print('Não é possivel fatorar um número negativo!')
            raise ValueError
    
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i

        print(f'O fatorial de {numero} é {resultado}')
    except ValueError as e:
        print(f' Erro: {e}')
    except Exception as e:
        print(f'Ocorreu um  erro inesperado: {e}')
calculadora_fatorail()

