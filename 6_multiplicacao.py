from random import randint

a = []
b = []

for i in range(10):
    a.append(randint(1, 51))
    
x = int(input("Digite um número inteiro: "))

for i in range(10):
    b.append(a[i] * x)
    
print("Lista A:", a)
print("Lista B:", b)