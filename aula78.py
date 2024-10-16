from itertools import count

contador = count(start=0, step=20)

#count() é um iterador

for i in contador:
    if i <= 100:
        print(f"Done! - {i}")
    else:
        break