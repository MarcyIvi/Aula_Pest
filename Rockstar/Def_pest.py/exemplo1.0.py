def positivo(num : float):
    if num > 0:
        return True
    else:
        return False

n = float(input('numero: '))

if positivo(n) == True:
    print('é positivo')

else: 
    print('não é positivo')