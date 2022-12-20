"""

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.

"""

from datetime import date
anoAtual = date.today().year

cadastro = dict()

print('-'*30)
print(f'{"VERIFICAÇÃO DE APOSENTADORIA":^30}')
print('-'*30)

cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
cadastro['Idade'] = anoAtual - ano
cadastro['Carteira de Trabalho'] = int(input('Número da Carteira de Trabalho (0 se não tiver): '))
print('-'*30)

if cadastro['Carteira de Trabalho'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salario'] = float(input('Salario: R$'))
    
    cadastro['Aposentadoria'] = 60 - (anoAtual - cadastro['Ano de Contratação']) 
    print('-'*30)

for k, v in cadastro.items():
    print(f'{k}: {v}')
print('-'*30)