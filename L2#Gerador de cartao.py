# Gerador de Cartão de Crédito:
### Crie um gerador de cartão de crédito que gere números de cartão de crédito válidos para a empresa de cartão de crédito especificada.
### Bônus: gere um número de cartão de crédito válido aleatoriamente para cada uma das empresas de cartão de crédito suportadas pelo seu aplicativo.

import random

import random

def gerar_cartao_credito(empresa):
    if empresa.lower() == "visa":
        prefixo = "4"
        numero_cartao = prefixo + ''.join(random.choice('0123456789') for _ in range(15))
    elif empresa.lower() == "mastercard":
        prefixo = "5"
        numero_cartao = prefixo + ''.join(random.choice('0123456789') for _ in range(15))
    elif empresa.lower() == "american express":
        prefixo = "3"
        numero_cartao = prefixo + ''.join(random.choice('0123456789') for _ in range(14))
    else:
        return "Empresa de cartão de crédito não suportada"
    
    data_validade = f"{random.randint(1, 12):02}/{random.randint(22, 30):02}"

    cvv = ''.join(random.choice('0123456789') for _ in range(3))

    return {
        "Número do Cartão": numero_cartao,
        "Data de Validade": data_validade,
        "CVV": cvv
    }

if __name__ == "__main__":
    empresas = ["Visa", "MasterCard", "American Express"]

    for empresa in empresas:
        cartao = gerar_cartao_credito(empresa)
        print(f"Empresa: {empresa}")
        print("Número do Cartão: ", cartao["Número do Cartão"])
        print("Data de Validade: ", cartao["Data de Validade"])
        print("CVV: ", cartao["CVV"])
        print()
