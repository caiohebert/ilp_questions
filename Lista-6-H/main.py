N, M = input().split()
N = int(N)
M = int(M)

matriz = []
for i in range(N):
    linha = [int(x) for x in input().split()]
    for fim in range(len(linha) - 1, 0, -1):
        for l in range(fim):
            if linha[l] > linha[l+1]:
                linha[l+1], linha[l] = linha[l], linha[l+1]
    matriz.append(linha)

Q = int(input())
consulta = [int(x) for x in input().split()]


for c in range(Q):
    salvos = 0
    for l in range (N):        
        esq = 0
        dir = len(linha) - 1
        while esq <= dir:
           meio = (esq + dir) // 2
           if matriz[l][meio] > consulta[c]:
               salvos += 1
               esq = meio + 1 
           elif consulta[c] >= matriz[l][meio]:
               esq = meio + 1 

    print(N*M - salvos)