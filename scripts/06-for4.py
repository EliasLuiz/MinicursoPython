lista = [1,2,3,4,5]
	
for i in range(len(lista)):
    lista[i] += 1
		
for indice, elemento in enumerate(lista):
    print("Posicao", indice,  "=", elemento)
