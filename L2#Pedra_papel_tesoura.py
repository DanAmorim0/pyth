# Pedra, Papel e Tesoura:
### Crie um jogo simples de pedra, papel e tesoura em que o computador escolhe aleatoriamente uma das três opções e o usuário tenta vencer o computador escolhendo sua própria opção.
### Bônus: dê ao usuário a opção de jogar com outro jogador humano.

import random

def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print("4. Sair")
        
        escolha_usuario = input("Digite o número da sua escolha: ")
        
        if escolha_usuario == "4":
            print("Obrigado por jogar!")
            break
        
        if escolha_usuario not in ["1", "2", "3"]:
            print("Escolha inválida. Tente novamente.")
            continue
        
        escolha_usuario = opcoes[int(escolha_usuario) - 1]
        escolha_computador = random.choice(opcoes)
        
        print(f"Você escolheu: {escolha_usuario}")
        print(f"O computador escolheu: {escolha_computador}")
        
        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (
            (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
            (escolha_usuario == "papel" and escolha_computador == "pedra") or
            (escolha_usuario == "tesoura" and escolha_computador == "papel")
        ):
            print("Você ganhou!")
        else:
            print("O computador ganhou!")

if __name__ == "__main__":
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    jogo_pedra_papel_tesoura()
