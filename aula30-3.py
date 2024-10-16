primeiro_nome = str(input("Digite seu primeiro nome: "))

if len(primeiro_nome) <= 4:
    print("Seu nome é curto")
elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print("Seu nome é comum")
elif len(primeiro_nome) > 6:
    print("Seu nome é muito grande")