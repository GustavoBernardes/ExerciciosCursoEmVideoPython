"""

Faça um programa que tenha uma função chamada maior(), que receba vários 
parâmetros com valores inteiros. Seu programa tem que analisar todos os 
valores e dizer qual deles é o maior.

"""

def maior(lista):
    count = maior = menor = 0
    
    for i in lista:
        if count == 0:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        count+=1
    
    print(f'Você digitou: {lista}\nO maior número é: {maior}\nO menor número é: {menor}')
    
num = list()

print('~'*50)
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    print('~'*50)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Desejá adicionar mais um número [S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('~'*50)
    
maior(num)
print('~'*50)