N, Q = input().split()   # qtd de selecionados e qtd total de candidatos
N = int(N)
Q = int(Q)

lista_nota = []
lista_id = []
selecionados_nota = []
selecionados_id = []
busca_nota = []
busca_id = []

for i in range(Q):
    X, Y = input().split()  #NQi e IdQi, nota e ID do candidato i
    X = int(X)
    Y = int(Y)
    lista_nota.append(X)
    lista_id.append(Y)
    
    
n = len(lista_nota)
for fim in range(n - 1, 0, -1):
    for l in range(fim):
        if lista_nota[l+1] > lista_nota[l]:
            lista_nota[l+1], lista_nota[l] = lista_nota[l], lista_nota[l+1]
            lista_id[l+1], lista_id[l] = lista_id[l], lista_id[l+1]
        if lista_nota[l+1] == lista_nota[l]:
            if lista_id[l+1] < lista_id[l]:
                lista_id[l], lista_id[l+1] = lista_id[l+1], lista_id[l]
            
for l in range(N):
    selecionados_nota.append(lista_nota[l])
    selecionados_id.append(lista_id[l])
    
p = len(selecionados_id)
for fim in range(p - 1, 0, -1):
    for l in range(fim):
        if selecionados_id[l+1] < selecionados_id[l]:
            selecionados_id[l+1], selecionados_id[l] = selecionados_id[l], selecionados_id[l+1]
            
C = int(input())
for i in range(C):
    x, y = input().split()   #NCi e IdCi, nota e ID do candidato i
    x = int(x)
    y = int(y)
    busca_nota.append(x)
    busca_id.append(y)
    
for i in range(len(busca_id)):
    esq = 0
    dir = len(selecionados_id) - 1
    while esq <= dir:
       meio = (esq + dir) // 2
       if selecionados_id[meio] == busca_id[i]:
           break
       elif busca_id[i] < selecionados_id[meio]:
           dir = meio - 1
       else:
           esq = meio + 1
           
    if selecionados_id[meio] == busca_id[i]:
       print("Sim")
    else:
       print("Nao")