def Range(inicio = 0, fim = 10, passo = 1):
    return list(range(inicio, fim, passo))

print(Range(1, 5))
print(Range(2))
print(Range())
print(Range(passo = 2))
print(Range(passo = 3, fim = 20))
print(Range(passo = 3, fim = 20, inicio = 1))
