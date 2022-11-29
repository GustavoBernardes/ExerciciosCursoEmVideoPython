"""

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""

import math

angulo = float(input('Digite um angulo: '))

print(f'''
      O angulo de {angulo}º tem o SENO: {math.sin(math.radians(angulo)):.2f}
      O angulo de {angulo}º tem o COSSENO: {math.cos(math.radians(angulo)):.2f}
      O angulo de {angulo}º tem o TANGENTE: {math.tan(math.radians(angulo)):.2f}
      ''')
