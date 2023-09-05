# criar um programa que solicta ao usuário insirir a quantidade de números de fibonacci que ele deseja ver e retorna os números de Fibonacci um por linha:

def fibonacci(numero_de_elementos):
    if numero_de_elementos == 1:
        return 0
    elif numero_de_elementos == 2:
        return [0,1]
    else:
        fibonacci = [0,1]
        for i in range(2, numero_de_elementos):
            novo_elemento_da_lista = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(novo_elemento_da_lista)
        return fibonacci
print(fibonacci(int(input('Digite o numero de vezes que a sequencia fibonacci deve aparecer: '))))