# 19/02/24

n1 = int(input('Insira um número:'))
n2 = int(input('Insira um número:'))
n3 = int(input('Insira um número:'))

if n1 == n2 or n2 == n3 or n1 == n3:
    print("Soma igual a zero.")

else: 
    res = n1 + n2 + n3
    print(f'O resultado da soma é {res}')
    