A = int(input())
lista = [int(x) for x in input().split()]
lista2 = []

for i in range(8):
    menor = min(lista)
    lista2.append(menor)
    del lista[lista.index(menor)]
    
print(*lista2)