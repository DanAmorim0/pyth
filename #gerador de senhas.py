#Gerador de Senhas:
### Crie um gerador de senhas que gera senhas aleatórias com base no comprimento especificado pelo usuário.
# Dica: use a biblioteca random do Python para gerar números aleatórios.
### Bônus: permita que o usuário especifique quantas letras, números e caracteres especiais a senha deve conter.
import random
import string

def gerar_senhas(letras, numeros, especiais):
    caracteres = string.ascii_letters + string.punctuation + string.digits
    carac = letras + numeros + especiais
    if carac < 4:
        print("A senha deve ter no minimo 4 caracteres")
        return None
    if letras + numeros + especiais > carac:
        print('Precisa de mais caracteres')
        return None
    senha = ''.join(random.choice(string.ascii_letters) for _ in range(letras))
    senha += ''.join(random.choice(string.digits) for _ in range(numeros))
    senha += ''.join(random.choice(string.punctuation) for _ in range(especiais))

    senha_aleatoria = ''.join(random.sample(senha, len(senha)))
    return senha_aleatoria

letras = int(input("Quantas letras você quer? "))
numeros = int(input("Quantos numeros você quer? "))
especiais = int(input("Quantos caracteres especiais você quer? "))

senha_aleatoria = gerar_senhas(letras, numeros, especiais)

if senha_aleatoria is not None:
    print("Senha gerada", senha_aleatoria)
else:
    print("Não foi possivel gerar a senha.")