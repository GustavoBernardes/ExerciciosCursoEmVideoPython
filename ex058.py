"""

Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

escolha = False

while not escolha:
    opcao = int(input('[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR\nO que deseja fazer? '))
    
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
        escolha = True
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
        escolha = True
    elif opcao == 3:
        print(f'O maior número digitado foi {max(num1, num2)}')
        escolha = True
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        escolha = True
    else:
        print('Opção Inválida!')