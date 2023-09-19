# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

def mult_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))

if mult_5(numero):
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")
