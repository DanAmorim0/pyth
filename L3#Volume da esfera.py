# Exercício 11 - Escreva um programa em que o usuário insere o valor do raio de uma esfera em m e o programa retorna o volume da esfera em litros.

def esfera():
    raio =float(input('Digite o raio de uma esfera em metros: '))
    volume = (4/3)*3.14 * raio**3 
    print(f'O volume da esfera é: V={volume:.2f}')
    litros = volume * 1000
    print(f'O volume da esfera em litros é: {litros:.2f}Listros')
esfera()
