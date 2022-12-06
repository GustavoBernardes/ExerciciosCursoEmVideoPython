"""

Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""

from datetime import date

anoAtual = date.today().year
menores = 0
maiores = 0

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    
    if anoAtual - ano >= 18:
        maiores += 1
    else:
        menores += 1
    
print(f'{maiores} pessoas são maiores de idade e {menores} menores de idade.')        