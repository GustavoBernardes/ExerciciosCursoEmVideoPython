"""

Crie um programa que faça o computador jogar Jokenpô com você.

"""

import random

escolha_jogador = int(input('''Escolha pedra, papel ou tesoura:
                    [ 1 ] - PEDRA
                    [ 2 ] - PAPEL
                    [ 3 ] - TESOURA
                    
                    Qual a sua escolha?
                    '''))

escolha_computador = random.randint(1, 3)

if escolha_jogador == 1:
    if escolha_computador == 2:
        print(f'''Você escolheu PEDRA e o computador PAPEL.
            
            PAPEL ganha de PEDRA!
            
            Você PERDEU!
            ''')
    elif escolha_computador == 3:
        print(f'''Você escolheu PEDRA e o computador TESOURA.
          
          PEDRA ganha de TESOURA!
          
          Você GANHOU!
          ''')
    else:
        print(f'''Você escolheu PEDRA e o computador PEDRA.
          
          PEDRA empata com PEDRA!
          ''')
elif escolha_jogador == 2:
    if escolha_computador == 1:
        print(f'''Você escolheu PAPEL e o computador PEDRA.
            
            PAPEL ganha de PEDRA!
            
            Você GANHOU!
            ''')
    elif escolha_computador == 3:
        print(f'''Você escolheu PAPEL e o computador TESOURA.
          
          PAPEL perde para TESOURA!
          
          Você PERDEU!
          ''')
    else:
        print(f'''Você escolheu PAPEL e o computador PAPEL.
          
          PAPEL empata com PAPEL!
          ''')
elif escolha_jogador == 3:
    if escolha_computador == 1:
        print(f'''Você escolheu TESOURA e o computador PEDRA.
            
            TESOURA perde para PEDRA!
            
            Você PERDEU!
            ''')
    elif escolha_computador == 2:
        print(f'''Você escolheu TESOURA e o computador PAPEL.
          
          TESOURA ganha de PAPEL!
          
          Você GANHOU!
          ''')
    else:
        print(f'''Você escolheu TESOURA e o computador TESOURA.
          
          TESOURA empata com TESOURA!
          ''')
else:
    print(f'ESCOLHA INVÁLIDA!')
