# Contador de Palavras:
### Faça um programa que conte quantas palavras há em uma frase inserida pelo usuário.
### Bônus: faça o programa retornar a frase com todas as letras maiúsculas e sem espaços em branco.

def cont():
    palavra = input('Digite uma frase aqui: ')
    separador = palavra.split()
    contador = len(separador)
    frase_sem_espaco = ''.join (separador)
    return f'A frase tem {contador} palavras. \n A frase escolhida foi: {palavra.title()}\n Frase sem espaço: {frase_sem_espaco}.'
resultado = cont()
print(resultado)