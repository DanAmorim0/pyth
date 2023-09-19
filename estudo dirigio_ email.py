# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.
def email_valido():
    email= input('DIGITE SEU EMAIL:').lower()
    if '@' in email:
        return True
    else:
        return False
print(email_valido())