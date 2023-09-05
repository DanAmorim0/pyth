#progromaquesolicita  ao usuario insirir umnúmero inteiro e retonra se o númrto é par ou ímpar.

'''def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'o número {numero} é ímpar.')
par_ou_impar(int(input('Digite um número inteiro: ')))

def mult_de_5(numb):
    if numb % 5 == 0:
        return True
    else:
        return False
numb = int(input('Digite um número inteiro: '))
print(mult_de_5(numb))'''

#programa que solicita ao usuário um numero e retorna se ele é múltiplo de 3 e 5.

def multiplo_de_5(nmr):
    if nmr % 5 == 0:
        return True #ou print(f'o número {nmr} é múltiplo de 5.')
    else:
        return False #print(f'o nrumero {nmr} não é multiplo de 5.')

def multiplo_de_3(nmr):
    nmr = int(input("Digite um número inteiro: "))
    if multiplo_de_5(nmr) and multiplo_de_3(nmr):
        print(f'O número {nmr} é múltiplo de 5 e 3.')
    elif multiplo_de_5(nmr):
        print(f'O número {nmr} é multiplo de 5.')
    elif multiplo_de_3(nmr):
        print(f'O número {nmr} é multiplo de 3')
    else:
        print(f'O número {nmr} não é multiplo de 5 e nem de 3.')