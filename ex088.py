"""

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.

"""

alunos = list()
count = 1

print('='*23)    
print(f'{"BOLETIM DIGITAL":^23}')
print('='*23)

while True:
    print(f'Cadastro do {count}º aluno(a)')
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])
    count+=1
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar mais um aluno? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    
alunos.sort()

print('='*23)    
print(f'{"ID":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*23)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') 
print('='*23)

escolha2 = ' '
while True:
    escolha2 = int(input('Mostrar nota de qual aluno? (999 se não quiser) '))
    
    if escolha2 == 999:
        break
    else:
        print(f'As notas de {alunos[escolha2][0]}, são: {alunos[escolha2][1]}')
        print('-'*23)

print('='*23)      
print('Programa encerrado')   