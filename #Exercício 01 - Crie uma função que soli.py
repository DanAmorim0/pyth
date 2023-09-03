

#Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplicação que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def subs(texto):
    return texto.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*').replace('A', '*').replace('E', '*').replace('I', '*').replace('O', '*').replace('Ua', '*')

print(subs(input('Digite a palavra: ')))

#Exercício 02 - Crie uma aplicação que solicite ao usuário digitar uma palavra e imprima no console a quantidade de caracteres que a palavra possui.

def contador(texto):
    return len(texto)

palavra = (input("Digite a palavra aqui: "))
print("Sua palavra tem: " + str(contador(palavra))+ " caracteres")

#Exercício 03 Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.

def contar_a(texto):
    return texto.replace('A', 'a').count('a')

palavra = (input("Digite a palavra: "))
print("Letra A, aparece um total de: " + str(contar_a(palavra))+ " vezes")

#Exercício 04 Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def maius(texto):
    return texto.upper()

nome = (input('Digite seu nome completo: '))
print(maius(nome))

#Exercício 05 Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras minúsculas.

def minus(texto):
    return texto.lower()

nome = (input('Digite seu nome completo: '))
print(minus(nome))

"""#Exercícios 06 Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.

def forma_nome(nome_completo):
    nome, sobrenome = nome_completo.split()
    nome_formatado = nome.upper() + sobrenome.lower()
    return nome_formatado
def nome(texto)
    nome_completo = input("Digite o seu nome e sobrenome: ")
    nome_sobrenome_formatado = forma_nome(nome_completo)
    print("Nome formatado:", nome_sobrenome_formatado)"""

"""#Exercícios 07 Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas. Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.

def tm_ncp(texto):
    nome_cpt = input('Digite seu nome completo: ')
    nome_usuario, sbrnome_usuario = nome_cpt.split()
    nome_cpt_mscl = nome_usuario.upper()
    sbrnome_usuario_mnscl = sbrnome_usuario.lower()
    tm_ncp = len(nome_cpt)
    print('O nome completo tem: ' + (tm_ncp)+ ' caracteres.'.format(tm_ncp))"""
    
"""#Exercício 08 Crie um programa que solicite apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:

def contar_palavras(texto):
    return len(texto.split())

def contar_vogais(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")

def substituir_python_por_java(texto):
    return texto.replace("Python", "Java")

def converter_para_minusculas(texto):
    return texto.lower()

def palavras_unicas(texto):
    return sorted(set(palavra.lower() for palavra in texto.split()))

def imprimir_ordem_alfabetica(texto):
    return sorted(texto.split(), key=str.lower)

def main():
    texto = input("Digite um texto: ")
    
    opcoes = {
        1: contar_palavras,
        2: contar_vogais,
        3: substituir_python_por_java,
        4: converter_para_minusculas,
        5: palavras_unicas,
        6: imprimir_ordem_alfabetica
    }
    
    opcao = int(input("Escolha uma opção:\n"
                     "1. Contar o número de palavras\n"
                     "2. Contar o número de vogais\n"
                     "3. Substituir Python por Java\n"
                     "4. Converter para minúsculas\n"
                     "5. Criar lista de palavras únicas\n"
                     "6. Imprimir palavras em ordem alfabética\n"))
    
    if opcao in opcoes:
        resultado = opcoes[opcao](texto)
        print("Resultado:", resultado)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()"""

#Exercicio 09 Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def remov_vog(texto):
    return texto.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print(remov_vog(input('Digite o texto aqui: ')))

#exercicio 10 Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def qnt_crt(texto):
    return len(texto)
txt = (input("Digite o texto: "))
print("Seu texto: " + str(qnt_crt(txt))+ " caracteres")

"""#exercicio 11 - DESAFIO DE ARTE ASCII

def main():
    caractere = input("Digite um caractere para o padrão de arte: ")
    altura = int(input("Digite a altura do padrão de arte (número inteiro positivo): "))

    if altura <= 0:
        print("Altura inválida. Por favor, insira um número inteiro positivo.")
        return

    for i in range(1, altura + 1):
        linha = caractere * i
        print(linha)

if __name__ == "__main__":
    main()"""