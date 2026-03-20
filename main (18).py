nota = [100, 50, 20, 10, 5, 2, 1]

N = int(input())

print(N)

for valor_nota in nota:
    quantidade = N // valor_nota
    print(f"{quantidade} nota(s) de R$ {valor_nota},00")
    N = N % valor_nota


