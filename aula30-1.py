numero_inteiro = input("Digite um número inteiro: ")

if numero_inteiro.isdecimal():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print("É par!")
    else:
        print("Não é par!")
else:
    print("Digite um número inteiro!")