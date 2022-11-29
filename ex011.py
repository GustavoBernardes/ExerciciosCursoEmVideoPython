largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
litros = area / 2

print(f'Para pintar essa parede será necessario: {litros:.0f} litros de tinta.')