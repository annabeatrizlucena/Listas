lista = []

n = int(input("Quantos elementos você deseja adicionar a sua lista? "))

for i in range(n):
    add = input("Digite aqui o que você deseja adicionar: ")
    lista.append(add)

print("Sua lista ficou dessa maneira: ", lista)
