velocidade = int(input('A quantos km/h você passou pelo radar? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa}!')
else:
    print('Você não foi multado!')