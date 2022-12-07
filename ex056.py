"""

Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Sexo inválido, tente novamente: ')).upper().strip()

print(f'Cadastro realizado com sucesso!\n{nome}, {idade} anos {sexo}')