import math

catOp = float(input('Comprimento do cateto oposto: '))
catAd = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(catOp, catAd)

print(f'O valor da hipotenusa é: {hip}')