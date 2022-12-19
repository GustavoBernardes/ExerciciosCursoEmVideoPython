"""

Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.

"""

print('-'*30)
print(f'{"Cadastro de pessoas":^30}')
print('-'*30)

grupo = list()
cadastros = list()
count = maiorPeso = menorPeso = 0


for i in range(0, 5):
    cadastros.append(str(input('Nome: ')).strip().capitalize())
    cadastros.append(int(input('Peso: ')))
    
    if len(grupo) == 0:
        maiorPeso = menorPeso = cadastros[1]
    else:
        if cadastros[1] > maiorPeso:
            maiorPeso = cadastros[1]
        if cadastros[1] < menorPeso:
            menorPeso = cadastros[1]
        
    grupo.append(cadastros[:])
    cadastros.clear()
    count+=1

print('-'*30)   
print(f'Você cadastrou {count} pessoas.')
print(f'O maior peso cadastrado foi {maiorPeso}kg de ', end='')
for pessoa in grupo:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso cadastrado foi {menorPeso}kg de ', end='')
for pessoa in grupo:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}]', end='')
print()
print('-'*30)
    