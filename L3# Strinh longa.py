# Exercício 20 - Crie um programa que solicita ao usuário inserir uma string longa contendo várias palavras. Em seguida, o programa deve imprimir:
# 1. uma string contendo apenas as palavras que começam com uma letra maiúscula.
# 2. uma string contendo apenas as palavras que terminam com uma vogal.
# 3. uma string contendo apenas as palavras que têm mais de 5 letras.
# 4. uma string contendo o inverso de cada palavra na string original. (Nota: não use a função reverse() do Python, faça isso manualmente!)

def string_longa():
    texto = input('Digite um texto longo aqui: ')
    palavras = texto.split()

    plv_maiuscula = []
    plv_vogal = []
    plv_5 = []
    plv_inverso = []

    for palavra in palavras:
        if palavra[0].isupper():
            plv_maiuscula.append(palavra)
        
        if palavra[-1] in 'aeiouAEIOU':
            plv_vogal.append(palavra)
        
        if len(palavra) > 5:
            plv_5.append(palavra)
        
        plv_inverso.append(palavra[::-1])

    print(f"Palavras que começam com letra maiúscula:", ' '.join(plv_maiuscula))
    print(f"Palavras que terminam com vogal:", ' '.join(plv_vogal))
    print(f"Palavras com mais de 5 letras:", ' '.join(plv_5))
    print(f"Inverso de cada palavra:", ' '.join(plv_inverso))

string_longa()

