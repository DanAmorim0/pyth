#Analisador de String:
### Faça um programa que analise uma string inserida pelo usuário e conte quantas letras maiúsculas, minúsculas, dígitos e caracteres especiais ela contém.
### Bônus: faça o programa retornar quantas palavras há na string.

def analisador_de_string(string):
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0
    palavras = len(string.split())

    for char in string:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1 
        elif char.isdigit():
            digitos += 1
        else:
            especiais += 1
    return maiusculas, minusculas, digitos, especiais, palavras
texto = input('Insira um texto aqui: ')

maiusculas, minusculas, digitos, espeicias, palavras = analisador_de_string(texto)
print(f'Letras maisculas: {maiusculas}')
print(f'Letras minusculas:{minusculas}')
print(f'Digitos: {digitos}')
print(f'Caracteres especiais: {espeicias}')
print(f'Quantidade de palavars no seu texto: {palavras}')