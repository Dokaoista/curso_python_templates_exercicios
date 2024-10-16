from itertools import count

amem = count()

for i in amem:
    if i >= 500000:
        break
    print(amem)