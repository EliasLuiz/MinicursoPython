constantes = {
    'pi' : 3.14159,
    'e' : 2.71828,
    'phi' : 1.61803
}

print('Constantes disponíveis: ')
for chave in constantes:
    print(chave, end = ' ')

print('\n\nValores das constantes:')
for chave, valor in constantes.items():
    print(chave, "=", valor)
