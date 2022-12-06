"""

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

"""

frase = str(input('Digite uma frase: ')).upper().strip()

palavras = frase.split()
fraseJunta = ''.join(palavras)
frasInvertida = ''

for i in range(len(fraseJunta) - 1, -1, -1):
    frasInvertida += fraseJunta[i]

if frasInvertida == fraseJunta:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
