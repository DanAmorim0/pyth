#Conversor de Temperatura:
### Crie um conversor de temperatura que permita ao usuário converter entre Celsius e Fahrenheit.
### Bônus: permita que o usuário especifique o número de casas decimais que deseja exibir.

def conversor():
    fahre = float(input('Quantos graus F°?: '))
    celsius = (fahre-32)/1.8
    resultado = '{:.2f}'.format(celsius)
    return print(f'Fahrenheit: {fahre}\n Conversão para graus Celsius: {resultado}°')

conversor()

def conversor_g_f():
    celsius = float(input('Quantos graus C°? '))
    fahre = (1.8*celsius)+32
    resultado = '{:.2f}'.format(fahre)
    return print(f'Graus Celsius: {celsius}°\n Conversão para Fahrenhei: {resultado}°.')

conversor_g_f()


selecao_user = int(input("Conversão de F°~C° digite 1. \n Conversão de C°~F° digite 2."))

if selecao_user == 1:
    conversor_graus_fire_celso()
elif selecao_user == 2:
    conversor_graus_celso_fire()
else:
    print("Digite somente entre 1 e 2.")






