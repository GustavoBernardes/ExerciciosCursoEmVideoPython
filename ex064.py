"""

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""

escolha = ''

print('=-='*20)

num = int(input('Digite um número: '))
listaNum = [num]

print('=-='*20)

while escolha != 'N':
    escolha = str(input('Deseja digitar mais um número [S/N]? ')).strip().upper()
    
    print('=-='*20)
    
    if escolha == 'S':
        num = int(input('Digite um número: '))
        listaNum += [num]  
        
        print('=-='*20)
    
print(f'''Você digitou {listaNum}
      A média deles é: {sum(listaNum)/len(listaNum)}
      O maior digitado foi: {max(listaNum)}
      O menor digitado foi: {min(listaNum)}
      ''')
print('=-='*20)
    
