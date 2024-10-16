lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

soma = [listaa + listab for listaa, listab in zip(lista_a, lista_b)]

print(soma)