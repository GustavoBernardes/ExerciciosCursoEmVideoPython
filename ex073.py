"""

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""

from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'Os números sorteados foram: {tupla}')
print(f'O maior número da tupla é: {max(tupla)}')
print(f'O menor número da tupla é: {min(tupla)}')