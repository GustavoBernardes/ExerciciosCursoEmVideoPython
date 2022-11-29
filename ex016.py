"""

Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""

from math import ceil, floor, trunc

num = float(input('Digite um número real: '))

print(f'O número {num} em sua forma inteira é: {int(num)}')
