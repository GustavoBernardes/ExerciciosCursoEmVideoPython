"""

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print(f'Sua nota foi {media:.2f}! Você foi APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua nota foi {media:.2f}! Você ficou de RECUPERAÇÃO!')
else:
    print(f'Sua nota foi {media:.2f}! Você foi REPROVADO!')
