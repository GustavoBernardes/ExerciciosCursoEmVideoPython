"""

Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.

"""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))

fim = termo + (10 - 1) * razao

for i in range(termo, fim, razao):
    print(f'{i}', end=' -> ')
    
print('ACABOU!')
    