# Calculadora de impostos:
### Crie um programa que permita ao usuário inserir o valor de uma compra e, em seguida, exiba o valor total da compra após adicionar o imposto.
### Bônus: permita que o usuário insira o valor do imposto a ser adicionado.

def calculadora_imposto():
    print("Qual o valor da sua compra?")
    compra = int(input(" "))
    imposto = int(input("Qual foi o valor do imposto do produto?"))
    soma = compra + imposto
    print(f'Você pagou {soma}$ no valor total da compra')
calculadora_imposto()