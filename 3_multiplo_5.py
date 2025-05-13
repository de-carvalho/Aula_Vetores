from random import randint

aleatorio = []

for i in range(20):
    aleatorio.append(randint(1, 51))
    if aleatorio[i] % 5 == 0:
        print(aleatorio[i], "é múltiplo de 5")

print(aleatorio)