# Exercício 9 - Escreva um programa que solicita ao usuário as dimensões de um retângulo e o programa retorna o perímetro e a área do retângulo.

def retangulo():
    base = int(input('Digite a base do retangulo: '))
    altura = int(input('Digite a altura do retâgulo: '))
    if base == altura:
        print('Você deu as dimensões de um quadrado: todos os lados iguais!')
        return
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f'A area do seu retângulo é: {area}')
    print(f'O perimetro do seu retângulo é: {perimetro}')
retangulo()
