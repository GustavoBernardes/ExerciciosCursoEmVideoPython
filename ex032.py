n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'{n1} \n{n2} \n{n3}')
    else: 
        print(f'{n1} \n{n3} \n{n2}')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'{n2} \n{n1} \n{n3}')
    else: 
        print(f'{n2} \n{n3} \n{n1}')
elif n3 > n1 and n3 > n2:
    if n2 > n1:
        print(f'{n3} \n{n2} \n{n1}')
    else: 
        print(f'{n3} \n{n1} \n{n2}')