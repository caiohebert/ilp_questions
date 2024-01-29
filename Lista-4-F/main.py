N = int(input())
X = [int(y) for y in input().split()]
lista = [0]*(max(X)+1)
novo = []

for l in range(len(X)):
    lista[X[l]] = 1

for l in range(len(lista)):
    if lista[l] == 1:
        novo.append(l)

print(*novo)