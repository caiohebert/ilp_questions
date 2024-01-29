Q, X, Y = input().split()
Q = int(Q)

lista = []

for i in range(Q):
    r, s = input().split()
    s = int(s)
    lista.append(r)
    lista.append(s)

n = len(lista)

if X == "N" and Y == "C":   #classfica por nome, menor p maior (A, B, C, D)
    for fim in range(n - 1, 0, -1):
        for l in range(1, fim, 2):
            if lista[l+1] < lista[l-1]:
                lista[l+1], lista[l-1] = lista[l-1], lista[l+1]
                lista[l], lista[l+2] = lista[l+2], lista[l]
    
if X == "N" and Y == "D":   #classfica por nome, maior p menor (Z, Y, X, W)
    for fim in range(n - 1, 0, -1):
        for l in range(1, fim, 2):
            if lista[l+1] > lista[l-1]:
                lista[l+1], lista[l-1] = lista[l-1], lista[l+1]
                lista[l], lista[l+2] = lista[l+2], lista[l]
    
if X == "L" and Y == "C":   #classfica por nível, menor p maior
    for fim in range(n - 1, 0, -1):
        for l in range(1, fim, 2):
            if lista[l+2] < lista[l]:
                lista[l+2], lista[l] = lista[l], lista[l+2]
                lista[l-1], lista[l+1] = lista[l+1], lista[l-1]


if X == "L" and Y == "D":   #classfica por nível, maior p menor
    for fim in range(n - 1, 0, -1):
        for l in range(1, fim, 2):
            if lista[l+2] > lista[l]:
                lista[l+2], lista[l] = lista[l], lista[l+2]
                lista[l-1], lista[l+1] = lista[l+1], lista[l-1]
                
for p in range(0, n, 2):
    print(lista[p], lista[p+1])