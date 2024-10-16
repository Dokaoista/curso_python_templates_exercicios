"""
Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da
funcao2 executada. Faça a funca1 executar duas funcoes que recebem um número
diferente de argumentos
"""

def funcao2():
    print("Amem")

def funcao(argumento):
    print(argumento)

def soma(numero_1, numero_2):
    print(numero_1 + numero_2)

def funcao1(funcao2, *args, **kwargs):
    return funcao2(*args, **kwargs)

resultado1 = funcao1(funcao, "Opa!")
resultado2 = funcao1(soma, 5, 5)

resultado1
resultado2