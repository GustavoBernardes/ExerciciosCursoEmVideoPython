"""

Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante 
o campeonato.

"""

jogador = dict()
gols = list()

print('-'*50)
print(f'{"DESEMPENHO JOGADOR":^50}')
print('-'*50)

jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))

for i in range(jogador["Partidas"]):
    gols.append(int(input(f'Quantos gol o {jogador["Nome"]} fez no {i+1}º jogo? ')))

jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)
print('-'*50)

print(f'O jogodar {jogador["Nome"]} marcos {jogador["Total de gols"]} gols em {jogador["Partidas"]} partidas.')
print('-'*50)

print('O desempenho dele em cada partida foi: ')
for i in range(len(jogador['Gols'])):
    print(f'Na {i+1}ª partida ele marcou: {jogador["Gols"][i]} gols')
print(f'Finalizando a temporada com um total de {jogador["Total de gols"]} gols.')
print('-'*50)