"""

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""

lista = []

for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    
maior = max(lista)
menor = min(lista)
    
print(f'O maior número digitado foi: {maior} e está na posição: {lista.index(maior)+1}.')
print(f'O menor número digitado foi: {menor} e está na posição: {lista.index(menor)+1}.')

