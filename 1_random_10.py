from random import randint

aleatorio = []
par = []
impar = []

for i in range(10):
    aleatorio.append(randint(1, 51))
    if aleatorio[i] % 2 == 0:
        par.append(aleatorio[i])
    else:
        impar.append(aleatorio[i])
    
print(aleatorio)
print(len(par), "números pares")
print(len(impar), "números ímpares")