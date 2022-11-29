"""

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
litros = area / 2

print(f'Para pintar essa parede será necessario: {litros:.0f} litros de tinta.')
