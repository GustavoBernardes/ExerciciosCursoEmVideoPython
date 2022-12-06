"""

Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

"""

num1 = float(input('Digite a medida da primeira reta: '))
num2 = float(input('Digite a medida da segunda reta: '))
num3 = float(input('Digite a medida da terceira reta: '))

if num1 == num2 and num3 == num1 and num3 == num2:
    print('Triângulo EQUILÁTERO.')
elif num1 == num2 or num3 == num2 or num3 == num1:
    print('Triângulo ISÓSCELES.')
else:
    print('Triângulo ESCALENO.')