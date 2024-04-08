def positivo(num : float):
    if num > 0:
        return 'positivo'
    else:
        return 'negativo'

n = float(input('numero: '))

if positivo(n) == 'positivo':
    print('é positivo')
else:
    print('é negativo')
