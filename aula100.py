def aumentar_porcentagem(preco):
    porcentagem = float(((10/100) + 1) * preco)
    return porcentagem

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = produtos.copy()

for produto in novos_produtos:
    preco = produto['preco']
    aumento = aumentar_porcentagem(preco)
    produto['preco'] = aumento ## aumento de preços

lista_ordenada = sorted(novos_produtos, key=lambda produto: produto['nome'], reverse=False) ## produtos ordenados pelo nome

produtos_ordenados_por_nome = lista_ordenada.copy()

preco_crescente = sorted(produtos_ordenados_por_nome, key=lambda produto: produto['preco'], reverse=False)

produtos_ordenados_por_preco = preco_crescente.copy()

for produto in produtos_ordenados_por_preco:
    print(f"{produto['nome']}: {produto['preco']:.2f}")