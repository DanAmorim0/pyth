#exercício com range e if em python
#crie um programa que solocite ao usário inserir um número inteiro positivo e o sisetma retorna se ele é múltiplo de 5 e retorne uma lista de todos os números ositivos menores que o número inserido que são múltiplos de 5.

def mult_5(numero):
    if numero % 5 == 0:
        print(f'O número {numero} é múltiplo de 5.')
        return True
    else:
        print(f'O número {numero} não é múltiplo de 5.')
        return False 

def solicitar_numero():
    numero_inserido = int(input('Digite um número inteiro positivos: '))
    if numero_inserido == '':
        print("voce nao digitou um numero.")
        return solicitar_numero()
    elif numero_inserido.isalpha():
        print('voce nao digitou um numero.')
        return solicitar_numero()
    elif int(numero_inserido)():
        

