from aula81 import produtos



def aumenta_idade(idade):
    idade['idade'] = round(idade['idade'] * 1.20)
    return idade

nova_idade = map(aumenta_idade, produtos)

print(list(nova_idade))