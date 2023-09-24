# Menu interativo
### Crie um aplicativo que exibe um menu interativo no console do usuário. Nesse menu, o usuário pode escolher entre as seguintes opções:
## 1. Calcular a sua idade em meses
## 2. Calcular a sua idade em dias
## 3. Calcular a sua idade em horas
## 4. Calcular a sua idade em minutos
## 5. Calcular a sua idade em segundos
## 6. Sair do programa

### Bônus: permita que o usuário insira a data atual e a data de seu nascimento.

from datetime import datetime

def calcular_idade_em_meses(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    idade_meses = diferenca.days // 30
    return idade_meses

def menu_interativo():
    while True:
        print('Escolha uma opção no menu interativo:')
        print('1. Calcular a sua idade em meses')
        print('2. Calcular a sua idade em dias')
        print('3. Calcular a sua idade em horas')
        print('4. Calcular a sua idade em minutos')
        print('5. Calcular a sua idade em segundos')
        print('6. Sair do programa')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '6':
            print('Fechando o programa...')
            break
        elif escolha in ['1', '2', '3', '4', '5']:
            data_nascimento = input('Digite sua data de nascimento (no formato YYYY-MM-DD): ')
            data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
            data_atual = datetime.now()

            if escolha == '1':
                idade_meses = calcular_idade_em_meses(data_nascimento, data_atual)
                print(f'Sua idade em meses é: {idade_meses} meses')
            elif escolha == '2':
                diferenca = data_atual - data_nascimento
                idade_dias = diferenca.days
                print(f'Sua idade em dias é: {idade_dias} dias')
            elif escolha == '3':
                diferenca = data_atual - data_nascimento
                idade_horas = diferenca.days * 24
                print(f'Sua idade em horas é: {idade_horas} horas')
            elif escolha == '4':
                diferenca = data_atual - data_nascimento
                idade_minutos = diferenca.days * 24 * 60
                print(f'Sua idade em minutos é: {idade_minutos} minutos')
            elif escolha == '5':
                diferenca = data_atual - data_nascimento
                idade_segundos = diferenca.days * 24 * 60 * 60
                print(f'Sua idade em segundos é: {idade_segundos} segundos')
        else:
            print('Opção inválida. Tente novamente.')


    print('Bem-vindo ao Menu Interativo de Cálculo de Idade!')
menu_interativo()
