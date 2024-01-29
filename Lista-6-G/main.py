N = int(input())
planetas = input().split()

X = int(input())
visitados = input().split()

matriz = []
coordenadas = [0]
distancia = 0

for i in range(N):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)

for i in range(X):
    esq = 0
    dir = N - 1
    while esq <= dir:
       meio = (esq + dir) // 2
       if planetas[meio] == visitados[i]:
           break
       elif visitados[i] < planetas[meio]:
           dir = meio - 1
       else:
           esq = meio + 1
    if planetas[meio] == visitados[i]:
        coordenadas.append(meio)

for l in range(len(coordenadas)-1):
    c1 = coordenadas[l]
    c2 = coordenadas[l + 1]
    distancia += matriz[c1][c2]

print(distancia)