def contar_digitos(n : int):
    contador = 0
    while n != 0:
        res = n % 10
        contador += 1
        n = (n - res) / 10
    return contador

n = int(input('Digite um número: '))

while n < 0: 
    n = int(input('Digite um número: '))
digitos = contar_digitos(n)
print(f'A quantidade de digitos: {digitos}')