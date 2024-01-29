N, M = input().split()
N = int(N)    # Nº de dimensões disponiveis
M = int(M)    # nº de dimen q morty quer ir

disp = [int(x) for x in input().split()]
morty = [int(y) for y in input().split()]

n = len(disp)
qtd = 0 

for i in range(len(morty)):
    esq = 0
    dir = n - 1
    while esq <= dir:
        meio = esq + (dir - esq) // 2
        if disp[meio] == morty[i]:
            break
        elif morty[i] < disp[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if disp[meio] == morty[i]:
        qtd += 1

print(qtd)