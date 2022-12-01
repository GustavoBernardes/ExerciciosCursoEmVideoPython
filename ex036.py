"""

Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""

num = int(input('Digite o número que deseja converter: '))
escolha = int(input('''Para qual base deseja converter? 
                    1 - Binário, 2 - Octal e 3 - Hexadecimal
                    '''))

if escolha == 1:
    print(f'O número {num} convertido para Binário é: {bin(num)}')
elif escolha == 2:
    print(f'O número {num} convertido para Octal é: {oct(num)}')
elif escolha == 3:
    print(f'O número {num} convertido para Hexadecimal é: {hex(num)}')
else:
    print('Escolha inválida!')