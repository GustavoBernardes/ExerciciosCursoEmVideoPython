"""

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade 
C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

"""

listaCadastros = list()
cadastro = dict()
somaIdade = mediaIdade = 0

print('-'*50)
print(f'{"CADASTRO PESSOAS":^50}')
print('-'*50)

while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while cadastro['Sexo'] not in 'MF':
        cadastro['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    cadastro['Idade'] = int(input('Idade: '))
    somaIdade += cadastro['Idade']
    print('-'*50)
    
    listaCadastros.append(cadastro.copy())
    cadastro.clear()
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar mais uma pessoa [S/N]? ')).strip().upper()[0]
    print('-'*50)
    if escolha == 'N':
        break
    

print(f'Você cadastrou {len(listaCadastros)} pessoas.')
print('-'*50)

mediaIdade = somaIdade / len(listaCadastros)
print(f'A média de idade das pessoas cadastradas é: {mediaIdade:.2f}')
print('-'*50)

print('As mulheres cadastradas são: ', end='')
for i in range(len(listaCadastros)):
    if listaCadastros[i]['Sexo'] == 'F':
        print(f'| {listaCadastros[i]["Nome"]}', end=' ')
print()
print('-'*50)

print('As pessoas com idade acima da média são: ', end='')
for i in range(len(listaCadastros)):
    if listaCadastros[i]['Idade'] > mediaIdade:
        print(f'| {listaCadastros[i]["Nome"]}', end=' ')    
print()
print('-'*50)