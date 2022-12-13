"""

Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

"""

print('='*20)
print('Cadastro de Produtros'.center(20))
print('='*20)

soma = contProd = precoBarato = i = 0
nomeBarato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    i+=1
    
    soma += preco
    
    if preco > 1000:
        contProd += 1
    
    if i == 1:
        precoBarato  = preco
        nomeBarato = nome
    else:
        if preco < precoBarato:
            precoBarato = preco
            nomeBarato = nome
               
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar mais um produto? [S/N] ')).strip().upper()
    if escolha == 'N':
            break
    
    print('='*20)
    
print(f'O total gasto na compra foi: R${soma:.2f}')
print(f'{contProd} produtos comprados custam mais de R$1000')
print(f'O produto mais barato que você comprou foi {nomeBarato} custando R${precoBarato:.2f}')