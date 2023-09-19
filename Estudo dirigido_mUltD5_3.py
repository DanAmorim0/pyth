def mult_5_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
if mult_5_3(numero):
    print(f"O número {numero} é múltiplo de 5 e de 3.")
else:
    print(mult_5_3(numero))