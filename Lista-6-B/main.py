P = int(input())
id_homens = [int(x) for x in input().split()]
id_mulheres = [int(y) for y in input().split()]

for i in range(P):
    maior = max(id_homens)
    menor = min(id_mulheres)
    print(maior, menor)
    del id_homens[id_homens.index(maior)]
    del id_mulheres[id_mulheres.index(menor)]