# Exercício 12 - Escreva um programa que contenha uma função com o seu nome que solicita ao usuário inserir um texto e retorna o número de letras que o texto contém que também compõem o seu nome.

def text(texto):
    nome = 'daniel'
    contador = 0
    for i in texto:
        if i.lower() in nome.lower():
            contador += 1
    return contador
texto_inserido = input('Digite um texto aleatorio: ')
qnt_letras = text(texto_inserido)
print(f'O texto contém {qnt_letras} letras  que também estão no nome "daniel".')