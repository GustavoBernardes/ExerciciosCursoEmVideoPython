"""

Faça um programa que tenha uma função chamada escreva(), que receba 
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.     

"""

def escreva(frase):
    tamanho = len(frase) + 4
    print('-'*tamanho)
    print(f'  {frase}')
    print('-'*tamanho)
    
entrada = str(input('Digite alguma coisa: '))

escreva(entrada)