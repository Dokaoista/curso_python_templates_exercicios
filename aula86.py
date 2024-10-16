dicionario_aleatorio = {
    'produto': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritório'
}


dc = {
    chave_aleatoria: valor.upper()
    if isinstance(valor, str) else valor
    for chave_aleatoria, valor in dicionario_aleatorio.items()
    if chave_aleatoria != 'categoria'
}

print(dc)