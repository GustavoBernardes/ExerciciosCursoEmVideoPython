"""

Faça um programa que tenha uma função chamada área(), que receba as dimensões 
de um terreno retangular (largura e comprimento) e mostre a área do terreno.

"""

def area(largura, comprimento):
    calculo = largura * comprimento
    
    print(f'A área do terreno {largura}x{comprimento} e de {calculo}m²')

print('-'*30)
print(f"{'CALCULO DE TERRENOS':^30}")
print('-'*30)

l = float(input('Largura (m):'))
c = float(input('Comprimento (m): '))

area(l, c)
print('-'*30)