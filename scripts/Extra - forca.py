#modulo do sistema, usado para limpar o console
import os
#modulo de para numeros aleatorios
from random import random

#lista de palavras disponiveis no jogo
palavras = ['cabelo', 'camelo', 'sapato', 'paralelepipedo', 'telefone']

#escolhe uma posicao aleatoriamente
num = int( random() * len(palavras) )
#le palavra escolhida
palavra = palavras[num]

#inicializa listas auxiliares como vazias
letrasusadas = []
acertos = 0

#enquanto nao tiver acertado todas as letras
while acertos < len(palavra):
    
    #limpa a tela
    os.system('cls')
    
    #para cada letra
    for i in palavra:
        #se foi escolhida imprime a letra
        if i in letrasusadas:
            print(i, end=' ')
        #se nao foi imprime underline
        else:
            print('_', end=' ')
            
    #imprime todas as letras ja usadas
    print('\nLetras usadas: %s' % letrasusadas)
    
    #le uma letra do usuario
    letra = input('Informe uma letra: ')
    #adiciona letra lida na lista de letras usadas
    letrasusadas.append(letra)
    
    #para cada vez que a letra ocorre na palavra
    for i in palavra:
        if i == letra:
            #adiciona um acerto
            acertos += 1
    

print('Palavra correta!')
print(palavra)
