#Calculadora de IMC (Índice de Massa Corporal):
### Crie uma calculadora que permite ao usuário calcular seu IMC com base em seu peso e altura.
### Bônus: responda se o usuário está acima, abaixo ou dentro do peso ideal.

def calculo_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura aqui: "))
    conta = peso/(altura * altura)
    imc = '{:.2f}'.format(conta)
    if float(imc) <= 16:
        return 'magreza grave', 'Seu imc é:',imc
    elif 16 < float(imc) <= 17:
        return 'magreza moderada','Seu imc é:', imc
    elif 17 < float(imc) <= 18.5:
        return 'magreza leve', 'Seu imc é:',imc
    elif 18.5 < float(imc) <= 25:
        return 'saudável', 'Seu imc é:',imc
    elif 25 < float(imc) <= 30:
        return 'sobrepeso', 'Seu imc é:',imc
    elif 30 < float(imc) <= 35:
        return 'obesidade grau 1','Seu imc é:', imc
    elif 35 < float(imc) <= 40:
        return 'obesidade grau 2', 'Seu imc é:',imc
    elif float(imc) >= 40:
        return 'obesidade grau 3','Seu imc é:', imc
    else:
        return 'IMC fora das faixa'
resultado = calculo_imc()
print(resultado)
