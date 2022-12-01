"""
Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.

"""

n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As medidas fornecidas formam um triângulo!')
else: 
    print('As medida não formam um triângulo!')