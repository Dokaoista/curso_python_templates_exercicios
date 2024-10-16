def funcao_return_outra():
    return print

a = funcao_return_outra()

print(id(a), id(print))