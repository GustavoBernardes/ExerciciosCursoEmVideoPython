"""

Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""

i = 1

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

while i < 10:
    print(f'{termo}', end='')
    print(' -> ' if i < 10 else '', end='')
    termo += razao
    i+=1

print(termo, end='')
print(' ACABOU!', end='')