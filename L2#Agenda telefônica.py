# Agenda Telefônica:
### Desenvolva um aplicativo de agenda telefônica que permita ao usuário adicionar, pesquisar, editar e excluir contatos.
### Bônus: armazene a agenda telefônica em um arquivo e carregue-a quando o aplicativo for iniciado.

def agenda_telefonica():
    agenda = []

    while True:
        print('\nMenu:')
        print('1. Adicionar contato')
        print('2. Pesquisar contato')
        print('3. Editar contato')
        print('4. Excluir contato')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            pesquisar_contato(agenda)
        elif opcao == '3':
            editar_contato(agenda)
        elif opcao == '4':
            excluir_contato(agenda)
        elif opcao == '5':
            print('Saindo da agenda telefônica. Até logo!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

def adicionar_contato(agenda):
    nome = input('Insira o nome que quer adicionar a agenda telefônica:')
    endereco = input('Insira o endereço quer quer adicionar a agenda telefônica:')
    telefone = input('Insira o telefone que quer adicionar a agenda telefônica:')
    email = input('Insira o email que quer adicionar a agenda:')

    contato = {
        'Nome': nome,
        'Endereço': endereco,
        'Telefone': telefone,
        'Email': email,
    }

    agenda.append(contato)
    print('Contato adicionado com sucesso!')

def pesquisar_contato(agenda):
    pesquisa = input('Digite o nome do contato que deseja pesquisar: ')
    resultados = []

    for i, contato in enumerate(agenda, 1):
        if pesquisa.lower() in contato['Nome'].lower():
            resultados.append((i, contato))

    if resultados:
        print('\nResultados da pesquisa:')
        for i, contato in resultados:
            print(f"{i}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")
    else:
        print('Nenhum resultado encontrado.')

def editar_contato(agenda):
    pesquisar_contato(agenda)
    indice = int(input('Digite o número do contato que deseja editar: ')) - 1

    if 0 <= indice < len(agenda):
        contato = agenda[indice]

        print('Editando contato:')
        print(f"Nome: {contato['Nome']}")
        print(f"Endereço: {contato['Endereço']}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Email: {contato['Email']}")

        contato['Nome'] = input('Novo nome: ')
        contato['Endereço'] = input('Novo endereço: ')
        contato['Telefone'] = input('Novo telefone: ')
        contato['Email'] = input('Novo email: ')

        print('Contato editado com sucesso!')
    else:
        print('Índice inválido.')

def excluir_contato(agenda):
    pesquisar_contato(agenda)
    indice = int(input('Digite o número do contato que deseja excluir: ')) - 1

    if 0 <= indice < len(agenda):
        contato = agenda.pop(indice)
        print(f"Contato '{contato['Nome']}' excluído com sucesso!")
    else:
        print('Índice inválido.')


agenda_telefonica()
