"""

Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

"""

i = 1

num = int(input('Digite um número: '))
steps = num

while i < steps:
    num *= i
    i+=1

print(f'O fatorial do número digitado é: {num}')