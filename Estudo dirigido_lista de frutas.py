# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.

def lista_de_frutas():
    list_frutas = []
    print('Digite SAIR, para fechar o programa.')

    while True:
        frutas = input('DIGITE AQUI AS FRUTAS QUE VOCÊ DESEJA COMRPAR: ')

        if frutas.lower() == 'sair':
            break

        list_frutas.append(frutas)
    
    if list_frutas:
        print('\nLista de frutas desejadas: ')
        for i in list_frutas:
            print(i)
    else:
        print('Voce não digitou nenhuma fruta.')

lista_de_frutas()