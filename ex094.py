"""

Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

"""

cadastros = list()
jogador = dict()
gols = list()

print('-'*50)
print(f'{"DESEMPENHO JOGADOR":^50}')
print('-'*50)

while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    jogador['Partidas'] = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))

    for i in range(jogador["Partidas"]):
        gols.append(int(input(f'Quantos gol o {jogador["Nome"]} fez no {i+1}º jogo? ')))

    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = sum(gols)
    
    cadastros.append(jogador.copy())
    jogador.clear()
    gols.clear()
    
    print('-'*50)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar mais um jogador [S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('-'*50)

print('-'*50)
print(f'{"LISTA DE JOGADOR":^50}')
print('-'*50)
print(f'{"ID":<4}{"NOME":<10}{"TOTAL DE GOLS":>8}')
for i in range(len(cadastros)):
    print(f'{i:<4}{cadastros[i]["Nome"]:<10}{cadastros[i]["Total de gols"]:>6}')
print('-'*50)

escolha = ' '
while True:
    escolha = int(input('Deseja visualizar o desempenho individual de algum jogador (999 caso não queira)? '))
    if escolha == 999:
        break
    
    print('-'*50)
    print(f'O desempenho de {cadastros[escolha]["Nome"]} em cada partida foi: ')
    
    for i in range(len(cadastros[escolha]["Gols"])):
        print(f'Na {i+1}ª partida ele marcou: {cadastros[escolha]["Gols"][i]} gols')
    print(f'Finalizando a temporada com um total de {cadastros[escolha]["Total de gols"]} gols.')
    print('-'*50)
print('-'*50)
print('PROGRAMA FINALIZADO')
print('-'*50)   