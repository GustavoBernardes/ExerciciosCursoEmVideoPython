"""

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou 
então o empréstimo será negado.

"""

valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos deseja pagar a casa? '))

prestacao = valorCasa / (tempo * 12)

salarioTrinta = salario * 0.3

if prestacao > salarioTrinta:
    print(f'''
          Empréstimo negado!
          
          A prestação da casa ficou em R${prestacao:.2f}, excedendo 30% do salário.
          
          Aumente as parcelas para que o empréstimo seja aprovado!
          ''')
else:
    print(f'''
          Empréstimo aprovado!
          
          A prestação da casa ficou em R${prestacao:.2f}!
          ''')