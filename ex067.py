"""

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""

from random import randint
from time import sleep

print('=-='*10)
print('JOGO DO PAR OU ÍMPAR'.center(30))
print('=-='*10)

i = 0

while True:
    escolha = int(input('Você quer PAR ou ÍMPAR?\n[ 1 ] - PAR\n[ 2 ] - ÍMPAR\n[ 3 ] - Encerrar programa\nQual sua escolha? '))
    if escolha == 3:
        break
    print('=-='*10)
    
    if escolha == 1:
        print('Você escolheu PAR, então eu sou ÍMPAR!')
        sleep(0.5)
        numJogador = int(input('Digite um número de 0 a 10: '))
        sleep(0.5)
        print('Minha vez de pensar em um número..')
        sleep(0.5)
        print('Pronto!')
        print('=-='*10)
        
        numComputador = randint(0, 10)
        
        soma = numComputador + numJogador
        
        if soma % 2 == 0:
            print(f'''
                  Você escolheu o número: {numJogador}
                  Eu escolhi o número: {numComputador}                 
                  {numJogador} + {numComputador} = {soma}
                  {soma} é um número PAR!
                  Você GANHOU!!! PARABÉNS!!                  
                  ''')
            print('=-='*10)
        else:
            print(f'''
                  Você escolheu o número: {numJogador}
                  Eu escolhi o número: {numComputador}                 
                  {numJogador} + {numComputador} = {soma}
                  {soma} é um número ÍMPAR!
                  Você PERDEU!!!                 
                  ''')
            print('=-='*10)
            break
    elif escolha == 2:
        print('Você escolheu ÍMPAR, então eu sou PAR!')
        sleep(0.5)
        numJogador = int(input('Digite um número: '))
        sleep(0.5)
        print('Minha vez de pensar em um número..')
        sleep(0.5)
        print('Pronto!')
        print('=-='*10)
        
        numComputador = randint(0, 10)
        
        soma = numComputador + numJogador
        
        if soma % 2 == 0:
            print(f'''
                  Você escolheu o número: {numJogador}
                  Eu escolhi o número: {numComputador}                 
                  {numJogador} + {numComputador} = {soma}
                  {soma} é um número PAR!
                  Você PERDEU!!!              
                  ''')
            print('=-='*10)
            break
        else:
            print(f'''
                  Você escolheu o número: {numJogador}
                  Eu escolhi o número: {numComputador}                 
                  {numJogador} + {numComputador} = {soma}
                  {soma} é um número ÍMPAR!
                  Você GANHOU!!! PARABÉNS!!!              
                  ''')  
            print('=-='*10)
    i+=1

print(f'PROGRAMA ENCERRADO!! Você ganhou {i} vezes.')
