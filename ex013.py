"""

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""

salario = float(input('Digite o salario: R$'))

acrescimo = salario + (salario * 0.15)

print(f'O salario com um acrescimo de 15% ficou: R${acrescimo:.2f}')
