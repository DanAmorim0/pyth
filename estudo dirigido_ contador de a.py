# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.
def text_a():
    texto = input('Digite uma frase ou um texto aqui: ').lower()
    contagem = 0
    for a in texto:
        if a == 'a':
            contagem += 1
    print(f"A letra 'a' aparece {contagem} vezes no texto/frase.")
text_a()