"""

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Santos.

"""

times = ('1º Palmeiras', '2º Internacional', '3º Fluminense', '4º Corinthians', '5º Flamengo', '6º Athetico-PR', 
         '7º Atlético-MG', '8º Fortaleza', '9º São Paulo', '10º América-MG', '11º Botafogo', '12º Santos', '13º Goiás', 
         '14º Bragantino', '15º Coritiba', '16º Cuiabá', '17º Ceará', '18º Atlético-GO', '19º Avaí', '20º Juventude')

print('='*35)
print('Os 5 primeiros times colocado são:')
for i in range(0, 5):
    print(times[i])
print('='*35)

print('Os últimos 4 colocados são:')
for i in range(16, 20):
    print(times[i])
print('='*35)

print('Os Times em ordem alfabética são: ')
print(sorted(times))
print('='*35)

print(f'A posição do Santos é : {times.index("12º Santos")+1}º posição')