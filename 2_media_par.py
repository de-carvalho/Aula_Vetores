from random import randint

aleatorio = []
parQuantidade = 0
soma = 0

for i in range(20):
    aleatorio.append(randint(1, 51))
    if aleatorio[i] % 2 == 0:
        parQuantidade += 1
        soma += aleatorio[i]

if parQuantidade > 0:
    media = soma / parQuantidade
else:
    media = 0
        
print(aleatorio)        
print(parQuantidade)
print(soma)
print(media)
