distancia = float(input('Qual a distância da viagem em km? '))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'Sua viagem de {distancia}km custará R${preco:.2f}')