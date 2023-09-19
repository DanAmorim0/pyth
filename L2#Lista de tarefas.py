#Lista de Tarefas:
### Desenvolva um aplicativo de lista de tarefas que permita ao usuário adicionar, marcar como concluída e remover tarefas.
### Bônus: armazene a lista de tarefas em um arquivo e carregue-a quando o aplicativo for iniciado.
def lista_de_tarefas():
    lista = []

    while True:
        print('Lista de tarefas: ')
        for i, tarefa in enumerate(lista):
            print(f'{i + 1}. {tarefa}')
        
        print('Opções:')
        print('1- Adicionar tarefas')
        print('2- Marcar tarefas como concluidas')
        print('3- Remover tarefas')
        print('4- Sair')
        opcao = input('Escolha uma opção:')

        if opcao == '1':
            nova_tarefa = input('Digite uma ou mais tarefas para adicionar a lista:')
            lista.append(nova_tarefa)
        
        elif opcao == '2':
            index = int(input('Digite o número da tarefa concluida: '))
            if 1 <= index <= len(lista):
                lista[index - 1]=f'{lista[index - 1]}(concluída)'
            else:
                print('Número inválido')
        elif opcao == '3':
            index = int(input('Digite o número da tarefa para remover: '))
            if 1 <= index <= len(lista):
                lista.pop(index -1)
            else:
                print('Número inválido.')
        elif opcao == '4':
            print('Fechando...')
            break
        else:
            print('Digite somente um número de 1 a 4.')
lista_de_tarefas()