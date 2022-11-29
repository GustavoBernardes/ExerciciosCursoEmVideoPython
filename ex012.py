"""

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""

preco = float(input('Digite o valor do produto: R$'))

desconto = preco - (preco * 0.05)

print(f'O valor do produto com 5% de desconto: R${desconto}')
