# Exercício 18 -  Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). 
# Peça ao usuário para adivinhar o número e, em seguida, diga a eles se eles adivinharam, se o número é menor que o seu palpite ou se número é maior que o seu palpite.
import random

def nrm_aleatorio():
    tentativas = 0
    numero = random.randint(1, 9)
    print('O programa pensou em um número aleatorio, agora você precisa tentar acertar o número (1 a 9)')
    while True:
        chute = int(input('Insira o número aqui:'))
        if chute == numero:
            print('Parabéns, você acertou!!!')
            print(f'Você teve {tentativas} tentativas ate certar!')
            sair = input('Quer continuar jogando?').lower()
            if sair == 'nao':
                return
        elif chute > numero:
            print("o chute é maior que o número pensado pela maquina")
            tentativas += 1
        elif chute < numero:
            print('O chute é menor que o número pensado pela maaquina')
            tentativas += 1
        else:
            print('Digite um número inteiro e positivo de 1 a 9!')
nrm_aleatorio()