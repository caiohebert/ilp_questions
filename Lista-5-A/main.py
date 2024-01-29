P = int(input())
L = 10
matriz = []
presente = 0

for i in range(L):
   linha = [int(x) for x in input().split()]
   if P in linha:
       presente = 1
   matriz.append(linha)

if presente == 1:
    print("sim")
else:
    print("nao")