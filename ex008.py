"""

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

"""

metros = float(input('Digite a medida em metros: '))

print(f'''
      Centimetros: {metros*100}cm
      Milimetros: {metros*1000}mm
      Kilometro: {metros/1000}km
      ''')
