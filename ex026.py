"""

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

"""

nome = str(input('Digite sem nome completo: ')).strip()

lista = nome.split()

print(f'Primeiro nome: {lista[0]}')
print(f'Ultimo nome: {lista[-1]}')
