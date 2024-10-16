carrinho = list()

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 12))
carrinho.append(('Produto 3', 54))
carrinho.append(('Produto 4', 80))
carrinho.append(('Produto 5', 70))
carrinho.append(('Produto 6', 109.99))

tabela_de_precos = sum([float(preco) for produto, preco in carrinho])

print(f"Preço total do carrinho: R${tabela_de_precos:.2f}")