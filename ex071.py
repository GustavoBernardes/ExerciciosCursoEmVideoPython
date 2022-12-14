"""

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""

numeros = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 
           'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    num = int(input('Qual número você deseja ver? (0 a 20) '))
    if 0 < num > 20:
        print('Escolha inválida! Tente novamente')
        break
    
    print(numeros[num])
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja ver mais um número? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break