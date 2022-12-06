"""

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

num = int(input('Digite um número: '))
tot = 0

for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')

print(f'\n\033[m0 número {num} foi divisivel {tot} vezes')

if tot == 2:
    print('Ele é um número PRIMO!')
else:
    print('Ele não é um número PRIMO!')