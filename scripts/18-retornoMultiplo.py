def RaizQuadradaCubica(valor):
    return valor ** (1/2), valor ** (1/3)

print(RaizQuadradaCubica(64))

a, b = RaizQuadradaCubica(64)
print(a, b)

_,  raiz = RaizQuadradaCubica(64)
print(raiz)

#seguindo a mesma ideia
a = 1
b = 2
a, b = b, a
print(a, b)
