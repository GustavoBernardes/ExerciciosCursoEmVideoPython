"""

Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.

"""

lista = []
i = 0

while True:
    num = int(input('Digite um número: '))
    i+=1
    
    lista.append(num)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja adicionar mais um número? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

lista.sort(reverse= True)
   
print(f'Você digitou {i} número.')
print(f'Os número digitados foram: {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado!')
else:
    print(f'O número 5 não foi digitado!')
    