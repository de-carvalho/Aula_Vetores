from random import randint

a = []
resultado = []

for i in range(10):
    a.append(randint(1, 51))
    if a not in resultado:
        resultado.append(a)
    
print(a)