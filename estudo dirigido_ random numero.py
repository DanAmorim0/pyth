# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

import random

def jogo_adivinha():
    numero_gerado = random.randint(0, 10)
    tentativas = 0
    while True:
        nrm_digitado = int(input('Tente acertar o número que a maquina pensou: '))
        if nrm_digitado == numero_gerado:
            print(f'Parabéns, você acertou o número! \nVocê tentou {tentativas}x.')
            break
        elif nrm_digitado < numero_gerado:
            print('O número digitado é menor que o número sorteado.')
            tentativas += 1
        elif nrm_digitado > numero_gerado:
            print('O número digitado é maior que o número sorteado.')
            tentativas += 1
print(jogo_adivinha())
