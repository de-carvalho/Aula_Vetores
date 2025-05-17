from random import randint

a = []
pares = []

for i in range(10):
    a.append(randint(1, 51))
    
for i in range(10):
    if a[i] % 2 == 0:
        pares.append(a[i])
        
print(a)
print(pares)