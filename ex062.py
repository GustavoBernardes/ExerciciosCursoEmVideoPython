"""

Escreva um programa que leia um número N inteiro qualquer e mostre 
na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8

"""

print('=-='*20)
print('SEQUÊNCIA DE FIBONACCI'.center(55))
print('=-='*20)

termos = int(input('Quantos termos deseja mostrar? '))

t1 = 0
t2 = 1
i = 3

print(f'{t1} -> {t2}', end='')

while i <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    
    i+=1
print('')
print('=-='*20)
