"""

Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.

"""

num = int(input('Digite o número que deseja saber a tabuada: '))

for i in range(0, 11):
    print(f'{i} x {num:2} = {i*num}')