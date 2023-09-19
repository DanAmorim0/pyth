# Calculadora de Idade:
### Crie um programa que recebe o ano de nascimento do usuário e calcula a idade atual.
### Bônus: faça o programa retornar o signo do usuário de acordo com o mês e dia do seu nascimento.
signos = ['aquario','peixes','aries','touro','gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio']

ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2023
mes_do_nascimento = int(input("Digite o mês em que nasceu: "))
dia_do_nascimento = int(input("Dia do nascimento: "))
idade = ano_atual - ano_de_nascimento
signos1 = (mes_do_nascimento -2) 
resultado = signos[signos1]

print(f"Sua idade é: {idade}")
print(f"Seu signo é: {resultado}")

