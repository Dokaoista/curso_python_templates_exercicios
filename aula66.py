lista = [1,2,3,4,5,6,7,8,9,10]

# lista_comprehension = [valor_a_ser_mostrado for valor_a_ser_mostrado in iterable]

lista_comprehension = [i*2 for i in lista]
lista_comprehension2 = [(valores1, valores2) for valores1 in lista for valores2 in range(3)]

print(lista_comprehension)
print(lista_comprehension2)