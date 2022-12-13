"""

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

"""

i = 1
contM = contH = contIdade = contIdadeF = 0

while True:
    print('*-*'*20)
    print(f'Cadastro da {i}ª pessoa')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
    print('*-*'*20)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar outra pessoa [S/N]? ')).strip().upper()[0]
        
    if escolha == 'N':
        break
    print('*-*'*20)
    
    if idade > 18:
       contIdade += 1
    elif sexo == 'F' and idade < 20:
        contIdadeF += 1
    
    if sexo == 'M':
        contH += 1
    elif sexo == 'F':
        contM += 1   

    i+=1
    
print(f'Você cadastrou {i} pessoas.\n{contIdade} pessoas tem mais de 18 anos.\n{contH} homens foram cadastrados.\n{contM} mulheres tem menos de 20 anos.')
    