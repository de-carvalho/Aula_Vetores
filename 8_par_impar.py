from random import randint

a = []
b = []
c = []

for i in range(20):
    a.append(randint(1, 51))

print(a)

for i in range(20):
    if a[i] % 2 == 0:
        b.append(a[i])
print(b)

for i in range(20):
    if a[i] % 2 != 0:
        c.append(a[i])

print(c)
    