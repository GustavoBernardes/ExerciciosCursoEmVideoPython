"""

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome 
do homem mais velho e quantas mulheres têm menos de 20 anos.

"""

mediaIdade = []
idade_mais_velho = 0
nome_mais_velho = ''
cont_mulheres = 0

for i in range(1, 5):
    print('='*20)
    print(f'CADASTRO {i}ª PESSOA: ')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    
    mediaIdade += [idade]
    
    if i == 1 and sexo == 'M':
        idade_mais_velho = idade
    else:
        if idade > idade_mais_velho and idade:
            nome_mais_velho = nome
            idade_mais_velho = idade
        else:
            nome_mais_velho = nome
            idade_mais_velho = idade
    
    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1

print('='*45)
print(f'A média de idade do grupo é: {sum(mediaIdade)/len(mediaIdade)}')
print(f'O homem mais velho é o: {nome_mais_velho} de {idade_mais_velho} anos.')
print(f'No grupo {cont_mulheres} mulher tem menos de 20 anos.')
print('='*45)