"""

Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""

frase = str(input('Digite uma frase: ')).strip().lower()

contador = frase.count('a')
primeira = frase.find('a')+1
ultima = frase.rfind('a')+1

print(f'A letra "A" aparece: {contador} vezes.')
print(f'A letra "A" aparece pela primeira vez: {primeira}')
print(f'A letra "A" aparece pela ultima vez: {ultima}')
