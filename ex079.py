"""

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

"""

lista = []


for i in range(0, 5):
    num = int(input('Digite um valor: '))   
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao+=1

print(f'\nOs valores digitados em ordem são: {lista}.')
            