"""

Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.

"""

matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]
SomaPares = SomaTerceira = 0
linhaDois = list()

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor na posição [{linha}, {coluna}]: '))

for linha in range(0, 3):
    SomaTerceira += matriz[linha][2]
     
    for coluna in range(0, 3):
        print(f'|{matriz[linha][coluna]:^5}| ', end='')
        
        if matriz[linha][coluna] % 2 == 0:
            SomaPares += matriz[linha][coluna]
        
        linhaDois.append(matriz[1][coluna]) 
    print()

maior = max(linhaDois)

print(f'A soma dos pares é: {SomaPares}')
print(f'A soma da terceira coluna é: {SomaTerceira}')
print(f'O maior valor da segunda linha é: {maior}')