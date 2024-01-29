N, M = (input().split())
N = int(N)
M = int(M)

matrizA = []
matrizB = []

for i in range(N):
    linha = [int(x) for x in input().split()]
    matrizA.append(linha)
    
for i in range(N):
    linha = [int(x) for x in input().split()]
    matrizB.append(linha)

for l in range(N):
    linha = []
    for c in range(M):
        elemento = matrizA[l][c] - matrizB[l][c]
        linha.append(elemento)
    print(*linha)