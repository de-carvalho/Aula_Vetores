from random import randint

a = []
soma = 0

for i in range(10):
    a.append(randint(1, 51))
for i in range(10):
    soma += a[i]
print(a)
print(soma)