from random import randint

numero = int(input("Digite um número: "))
aleatorio = []

for i in range(20):
    aleatorio.append(randint(1, 51))
    if aleatorio[i] % numero == 0:
        print(aleatorio[i], "é múltiplo de", numero)
print(aleatorio)