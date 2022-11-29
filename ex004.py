entrada = input('Digite algo: ')

print(type(entrada))
print(f'A sua entrada é um número? {entrada.isnumeric()}')
print(f'A sua entrada é um texto? {entrada.isalpha()}')
print(f'A sua entrada está maiúscula? {entrada.isupper()}')
print(f'A sua entrada está minúscula? {entrada.islower()}')
print(f'A sua entrada começa com letra maiúscula? {entrada.istitle()}')