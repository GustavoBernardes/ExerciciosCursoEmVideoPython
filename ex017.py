"""

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

"""

import math

catOp = float(input('Comprimento do cateto oposto: '))
catAd = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(catOp, catAd)

print(f'O valor da hipotenusa é: {hip}')
