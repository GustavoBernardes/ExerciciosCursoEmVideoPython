"""

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""

lista = []
listaPAR = []
listaIMPAR = []

for i in range(0, 5):
    num = int(input('Digite um número: '))
    
    lista.append(num)
    
    if num % 2 == 0:
        listaPAR.append(num)
    else:
        listaIMPAR.append(num)

print(f'''
      Você digitou {lista} esses números.
      Os números pares são: {listaPAR}
      Os números impares são: {listaIMPAR}
      ''')