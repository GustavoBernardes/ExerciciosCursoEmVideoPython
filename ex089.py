"""

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.

"""

aluno = dict()


print('-'*20)
print('BOLETIM DIGITAL')
print('-'*20)
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input('Média: '))
print('-'*20)

if aluno['media'] >= 6:
    aluno['situacao'] = 'APROVADO'
    print(f'O aluno {aluno["nome"]} tem média {aluno["media"]}.')
    print('Situação: APROVADO')
elif 5 <= aluno["media"] < 6:
    aluno['situacao'] = 'RECUPERAÇÃO'
    print(f'O aluno {aluno["nome"]}, com média {aluno["media"]}.')
    print('Situação: RECUPERAÇÃO')
else:
    aluno['situacao'] = 'REPROVADO'
    print(f'O aluno {aluno["nome"]}, com média {aluno["media"]}.')
    print('Situação: REPROVADO')

print('-'*20)
