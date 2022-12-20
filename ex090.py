"""

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.

"""

from random import randint
from operator import itemgetter

print('-'*40)
print(f"{'JOGO DE DADOS':^40}")
print('-'*40)

resultado = {"Jogador 1" : (randint(1, 6)),
             "Jogador 2" : (randint(1, 6)),
             "Jogador 3" : (randint(1, 6)),
             "Jogador 4" : (randint(1, 6))}

for k, v in resultado.items():
    print(f'O {k} tirou {v} no dado.')
print('-'*40)

ranking = list()
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)

print(f"{'O RANKING FICOU:':^40}")
print('-'*40)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
print('-'*40)
