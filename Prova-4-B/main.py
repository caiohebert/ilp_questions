N = int(input()) 
S = int(input()) 
matriz1 = []

for l in range(S):
    linha = [int(x) for x in input().split()]
    matriz1.append(linha)

matriz2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for l in range(4):
    matriz2[l] = [y * N for y in matriz2[l]] 

for l in range(S):
    linha2 = matriz1[l][0] - 1
    coluna2 = matriz1[l][1] - 1
    matriz2[linha2][coluna2] = matriz1[l][2]

for l in range(4):
    print(*matriz2[l])