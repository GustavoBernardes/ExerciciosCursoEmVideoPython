"""

Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""

print('='*25)
print('CAIXA ELETRÔNICO')
print('='*25)

saque = int(input('Qual valor deseja sacar? R$'))

cedulas = 50
total = 0

while True:
    if saque >= cedulas:
        saque -= cedulas
        total+=1
    else:
        if total > 0:
            print(f'Sacando {total} notas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        
        total = 0
        
        if saque == 0:
            break

print('='*25)
