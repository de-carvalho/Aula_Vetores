from random import randint

lista = []

for i in range(10):
    lista.append(randint(1, 51))

for j in range(len(lista)):
    menor = j    
    for k in range(j + 1, len(lista)):
        if lista[k] < lista[menor]:
            menor = k      
    if menor != j:
        lista[j], lista[menor] = lista[menor], lista[j]
    
print("Lista ordenada:", lista)