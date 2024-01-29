N, M = input().split()
N = int(N)
M = int(M)
matriz = []

for i in range(N):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)
   
P = int(input())
qtd = 0

for l in range(N):
    for c in range(M):
        if matriz[l][c] == P:
            qtd += 1
print("Ash pegou", qtd, "pokemon")