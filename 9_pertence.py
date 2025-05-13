from random import randint

a = []
num = int(input("Digite um número inteiro: "))

for i in range(10):
    a.append(randint(1, 51))
    
print("Vetor: ", a)

if num == a[i]:
    print("O número pertence ao vetor")
else:
    print("O número não pertence ao vetor")