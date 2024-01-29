N = int(input())    # qtd de planetas visitados 
codigos = [int(x) for x in input().split()]
n_planetas = [int(y) for y in input().split()]    #elemento a ser procurado

# se for 0, encerra o programa.

for i in range(len(n_planetas)):   #n_planetas[i] é o elemento a ser procurado
    esq = 0
    dir = N - 1
    if n_planetas[i] == 0:
        break
    while esq <= dir:
       meio = (esq + dir) // 2
       if codigos[meio] == n_planetas[i]:
           break
       elif n_planetas[i] < codigos[meio]:
           dir = meio - 1
       else:
           esq = meio + 1
           
    if codigos[meio] == n_planetas[i]:
       print(meio)
    else:
       print("Nao foi visitado ainda")