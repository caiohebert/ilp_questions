N = int(input())
E = [int(x) for x in input().split()]

es = [1, 2, 3, 4, 5, 6, 7]
encontradas = []

for l in range(N):
    if E[l] in es:
        encontradas.append(E[l])

orden = sorted(encontradas)


if orden == es:
    print(*orden)
    print("Saia Shenlong e realize o meu desejo")
else:
    print(*orden)
    print("Nao encontramos todas")