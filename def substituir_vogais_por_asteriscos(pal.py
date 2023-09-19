def substituir_vogais_por_asteriscos(palavra):
    vogais = "aeiouAEIOU"
    palavra_substituida = ""
    
    for letra in palavra:
        if letra in vogais:
            palavra_substituida += "*"
        else:
            palavra_substituida += letra
    
    return palavra_substituida

def main():
    palavra = input("Digite uma palavra: ").lower()
    palavra_substituida = substituir_vogais_por_asteriscos(palavra)
    print("Palavra com vogais substituídas:", palavra_substituida)

if __name__ == "__main__":
    main()