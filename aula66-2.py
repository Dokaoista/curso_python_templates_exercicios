nomes = ["Kelvyn", "Jorge", "Morgana", "Arlequina", "Paulo"]

lista_comprehension = [nome if nome == "Kelvyn" else 'Não é Kelvyn' for nome in nomes]
lista_comprehension2 = [(x, "Amem") for x in nomes]

print(lista_comprehension2)