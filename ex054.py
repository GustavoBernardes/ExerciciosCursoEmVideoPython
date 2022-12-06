"""

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""

lista = []

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa:'))
    
    lista += [peso]
    
print(sorted(lista))