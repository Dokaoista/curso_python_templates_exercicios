def percentual(numero, porcentagem):
    percentual = porcentagem/100
    resultado = numero + (numero * percentual)
    return f"{resultado:.0f}"

funcao = percentual(50, 10)

print(funcao)