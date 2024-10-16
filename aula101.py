def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa(funcao, *args):
    yield from soma() ## adiando uma função
    return funcao(*args)

soma_com_cinco = executa(soma, 5)