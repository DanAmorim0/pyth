# Gerador de Sim ou Não:
### Crie um programa que permita ao usuário inserir uma pergunta e, em seguida, exiba uma resposta aleatória de sim ou não.
### Bônus: adicione a opção talvez ao gerador de respostas.

import random

def gerador_de_resposta():
    pergunta = input('Digite uma pergunta aleatoria: ').lower()
    resposta = ['sim', 'não', 'talvez']

    if pergunta != '':
        resposta = random.choice(resposta)
        print(resposta)
    else:
        print('Por favor, faça uma pergunta.')

gerador_de_resposta()