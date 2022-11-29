"""

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

dias = int(input('Digite a quantidade de dias que o carro ira ser alugado: '))
km = float(input('Digite a quantidade de km que o carro percorera: '))

vf = ((dias * 60) + (km * 0.15))

print(f'O valor de aluguel desse carro ficou em: R${vf}')
