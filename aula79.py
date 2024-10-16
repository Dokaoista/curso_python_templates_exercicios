from itertools import permutations, combinations, product
from math import prod

nomes = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in product(nomes, repeat=2):
    print(grupo)