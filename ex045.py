"""

Faça um programa que mostre na tela uma contagem 
regressiva para o estouro de fogos de artifício, indo de 10 até 0, 
com uma pausa de 1 segundo entre eles.

"""

from time import sleep

tempo = int(input('Digite qual número deseja começar a contagem: '))

for i in range(tempo, -1, -1):
    print(i)
    sleep(1)

sleep(0.5)   
print('FIM!')