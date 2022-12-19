"""

Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

"""

from random import randint

numeros = list()
jogos = list()
i = 1

print('='*24)
print(f'{"SORTEIO MEGA SENA":^24}')
print('='*24)

quantidade = int(input('Quantos jogos desejá criar? '))

while i <= quantidade:
    count = 0
    while True:
        num = randint(1, 60)
        
        if num not in numeros:
            numeros.append(num)
            count+=1
        
        if count >= 6:
            break
           
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    i+=1

print('='*24)
print('Os jogos sorteados são: ')
print('='*24)
    
for n, l in enumerate(jogos):
    print(f'Jogo {n+1}: {l}') 