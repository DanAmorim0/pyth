# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.

def c_area(raio):
    return 3.14 * raio ** 2

def c_perimetro(raio):
    return 2 * 3.14 * raio

def raio_circulo():
    try:
        raio = float(input('Digite o raio de um cículo em metros: '))
        area = c_area(raio)
        perimetro = c_perimetro(raio)

        print(f'A area do circulo é {area:.2f} m²')
        print(f'O perimetro do círculo é {perimetro:.2f}m')
    except ValueError:
        print('Insira um valor valido para o raio.')

raio_circulo()    