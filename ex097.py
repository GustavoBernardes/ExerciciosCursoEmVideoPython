"""

Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa 
tem que realizar três contagens através da função criada:                                                                                        
a) de 1 até 10, de 1 em 1                
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada

"""

from time import sleep

def contador(inicio, fim, passo):
    
    if passo < 0:
        passo*=-1
    if passo == 0:
        passo = 1
    
    print('-'*40)
    print(f'A contagem de {inicio} até {fim} com passo de {passo}.')
    
    count = inicio
    
    if inicio < fim:
        while count <= fim:
            print(f'{count} | ', end='', flush=True)
            count+=passo
            sleep(0.5)
        print('FIM!')
        print('-'*40)
    else:
        while count >= fim:
            print(f'{count} | ', end='', flush=True)
            count-=passo
            sleep(0.5)
        print('FIM!')
        print('-'*40)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de definir um contador!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
