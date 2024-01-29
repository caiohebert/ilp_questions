N = int(input())
lista = []

for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    lista.append(x)
    lista.append(y)
    
n = len(lista)
for fim in range(n - 1, 0, -1):
    for l in range(1, fim, 2):
        if lista[l+2] > lista[l]:
            lista[l], lista[l+2] = lista[l+2], lista[l]
            lista[l-1], lista[l+1] = lista[l+1], lista[l-1]
            
for p in range(0, n, 2):
    print(lista[p], lista[p+1])