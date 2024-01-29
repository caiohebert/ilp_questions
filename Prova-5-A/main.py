#ano-mes-dia (tudo junto), retornas lista de datas em ordem crescente
N = int(input())
lista = []

for i in range(N):
    x = int(input())
    lista.append(x)
    
for fim in range(N - 1, 0, -1):
    for i in range(0, fim):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

for y in range(N):
    print(lista[y])