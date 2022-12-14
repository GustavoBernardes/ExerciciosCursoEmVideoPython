"""

Crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre uma listagem de preços, 
organizando os dados em forma tabular.

"""

listaProdutos = ('Celular', 2999.99,
                 'Controle PS5', 249.99,
                 'Televisão', 7500.00,
                 'Sofá', 1399.99,
                 'Mesa de Jantar', 999.99,
                 'Quadro Decoração', 50.00,
                 'Cama', 890.00)

print('-'*50)
print(f'{"LISTA DE COMPRAS":^50}')
print('-'*50)

for i in range(0, len(listaProdutos)):
    if i % 2 == 0:
        print(f'{listaProdutos[i]:<40}', end='')
    else:
        print(f'R${listaProdutos[i]:>8.2f}')
print('-'*50)