"""

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""

print('=-='*10)
print('TABUADA'.center(30))
print('=-='*10)

while True:
    num = int(input('Qual número deseja ver a tabuada? '))
    print('=-='*13)
    
    if num < 0:
        break
    
    for i in range(0, 11):
        print(f'{num} x {i} = {num * i}')
        i+=1
    print('=-='*13)

print('PROGRAMA ENCERRADO!')