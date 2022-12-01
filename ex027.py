from random import randint

numComputador = randint(0, 5)

numJogador = int(input('Tente adivinhar o número que o computador pensou: '))

if numJogador == numComputador:
    print(f'PARABÉNS VOCÊ ACERTOU!! O número que o computador pensou era: {numComputador}')
else:
    print(f'VOCÊ ERROU!! O número que o computador pensou era: {numComputador}')