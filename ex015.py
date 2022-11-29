dias = int(input('Digite a quantidade de dias que o carro ira ser alugado: '))
km = float(input('Digite a quantidade de km que o carro percorera: '))

vf = ((dias * 60) + (km * 0.15))

print(f'O valor de aluguel desse carro ficou em: R${vf}')