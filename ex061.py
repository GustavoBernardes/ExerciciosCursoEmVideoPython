"""

Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

i = 1

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
ultimoTermo = 10
total = 0

while ultimoTermo != 0:
    total+=ultimoTermo  
    while i <= total:
        print(f'{termo}', end='')
        print(' -> ' if i < total else '', end='')
        termo += razao
        i+=1
        
    ultimoTermo = int(input(' Deseja ver mais quantos termos? '))

print(termo, end='')
print(' ACABOU!', end='')