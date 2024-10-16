from time import sleep
import sys

lista = [0,1,2,3,4,5]

#lista transformada em iterador

lista = iter(lista)

print(next(lista))

#geradores são usados para processos mais pesados, por não guardarem os valores na memória

def gerador():
    for numero in range(1, 101):
        yield numero
        sleep(0.1)


#Pode-se usar '()' em list comprehension para dizer que está usando um gerador

list_comprehension = [x for x in range(10000)] # list comprehension sem usar gerador
list_comprehension_gerador = (x for x in range(100000000000000000000000000000)) # list comprehension usando gerador

print(sys.getsizeof(list_comprehension))
print(sys.getsizeof(list_comprehension_gerador))