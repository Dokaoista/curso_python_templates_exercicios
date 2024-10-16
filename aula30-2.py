hora = str(input("Digite a hora atual: "))

if float(hora) >= 18:
    print("Boa noite!")
elif float(hora) >= 12:
    print("Boa tarde!")
elif float(hora) >= 0:
    print("Bom dia!")