"""

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""

from datetime import date

data_atual = date.today()

anoNascimento = int(input('Em qual ano você nasceu? '))

idade = data_atual.year - anoNascimento

if idade == 18:
    print('Está na hora de se Alistar!')
elif idade > 18:
    print('Já passou da idade de se Alistar!')
else:
    print(f'Ainda não é a hora de se Alistar! Ainda faltam {18 - idade} anos.')