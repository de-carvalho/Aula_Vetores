from random import randint

aleatorio = []  
opcao = int(input("Escolha 1 para ordem direta ou 2 para ordem inversa: "))

for i in range(10):
    aleatorio.append(randint(1, 51))
    
print(aleatorio)
    
if opcao == 1:
    print("Ordem direta:")
    for i in range(10):
        print(aleatorio[i], end=" ")
        
elif opcao == 2:
    print("Ordem inversa:")
    for i in range(9, -1, -1):
        print(aleatorio[i], end=" ")

else:
    print("Opção inválida.")