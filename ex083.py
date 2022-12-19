"""

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.

"""

aberto = fechado = 0

expressao = str(input('Digite a expressão: '))

for i in expressao:
    if i == '(':
        aberto+=1
    elif i == ')':
        fechado+=1
    
if aberto == fechado:
    print('A sua expressão está correta!')
elif aberto > fechado:
    print('A sua expressão está errada! Faltou fechar alguns parenteses.')
elif aberto < fechado:
    print('A sua expressão está errada! Você fechou mais parenteses do que o necessario.')
