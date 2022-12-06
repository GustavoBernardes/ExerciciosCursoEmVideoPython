"""

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

"""

preco = float(input('Digite o preço do produto:  R$'))
escolha = int(input('''Escolha a forma de pagamento:
                    1 - À vista dinheiro/cheque (10% de desconto)
                    2 - À vista no cartão (5% de desconto)
                    3 - Em até 2x no cartão (20% de juros)
                    4 - Em até 3x no cartão (20% de juros)
                    '''))

if escolha == 1:
    preco = preco - (preco * 0.1)
    print(f'O preço do produto para pagamento à vista no dinheiro é: R${preco:.2f}')
elif escolha == 2:
    preco = preco - (preco * 0.05)
    print(f'O preço do produto para pagamento à vista no cartão é: R${preco:.2f}')
elif escolha == 3:
    preco = preco - (preco * 0.2)
    parcela = preco / 2
    print(f'O preço do produto para pagamento em duas vezes no cartão será duas parcelas de: R${parcela:.2f} \nTotalizando R${preco:.2f}')
elif escolha == 4:
    preco = preco - (preco * 0.2)
    parcela = preco / 3
    print(f'O preço do produto para pagamento em três vezes no cartão será três parcelas de: R${parcela:.2f} \nTotalizando R${preco:.2f}')
else:
    print('Escolha inválida!')