contador1 = list()
contador2 = list()

while True:
    for numero in range(0, 9):
        contador1.append(numero)
    for i in range(10, 1, -1):
        contador2.append(i)
    break

for indice, numero in zip(contador1, contador2):
    print(indice, numero)