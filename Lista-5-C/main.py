N, M = input().split()
N = int(N)
M = int(M)

matriz1 = []

for i in range(N):
    linha = [int(x) for x in input().split()]
    matriz1.append(linha)

A = int(input())
matriz2 = []

for i in range(A):
    linha = [int(x) for x in input().split()]
    matriz2.append(linha)

kill = 0
falha = 0

for l in range(A):
    linha1 = matriz2[l][0]
    coluna1 = matriz2[l][1]
    matriz1[linha1-1][coluna1-1] = 0
    
for l in range(N):
    for c in range(M):
        if matriz1[l][c] == 1:
            falha = 1
            break
        
if falha == 1:
    print("ILL BE BACK")
else:    
    print("HASTA LA VISTA BABY")