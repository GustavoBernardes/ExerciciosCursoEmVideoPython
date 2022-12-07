"""

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.

"""

from time import sleep
from random import randint

print('='*35)
print('BEM VINDO(A) AO JOGO DE ADIVINHA!'.center(35))
print('='*35)
print('\n')

print('Estou pensando em um número..')
sleep(2)
print('PRONTO! Número escolhido. o número escolhido está entre 0 e 10!')
print('='*35)
print('\n')

numComputador = randint(1, 10)
countTentativas = 1

numJogador = int(input('Qual número você acha que eu pensei? '))

if numJogador != numComputador:
    while numJogador != numComputador:
        numJogador = int(input('ERROU!!! Tente novamente: '))
        countTentativas += 1 
        if numJogador == numComputador:
            print('\n')
            print('='*35)
            print(f'Parabéns!! Você acertou, o número que eu tinha pensado era: {numComputador}!\nVocê precisou de {countTentativas} tentativas!')
            print('='*35)    
else:
    print('\n')
    print('='*35)
    print(f'Parabéns!! Você acertou, o número que eu tinha pensado era: {numComputador}!\nVocê precisou de {countTentativas} tentativas!')
    print('='*35)