"""

Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""

palavras = ('Grátis', 'Criar', 'Carro', 'Barco', 'Nome', 'Dente', 'Cavalo', 'Lapís', 'Helicoptero')

for palavra in palavras:
    print(f'\nNa palavra: {palavra}, temos essas vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aàáâãeéèêiíìoóòôõu':
            print(letra, end=' ')