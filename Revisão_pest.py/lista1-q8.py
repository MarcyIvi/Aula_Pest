#05/02/24

x1 = float(input('Insira o valor de x1: '))
y1 = float(input('Insira o valor de y1: '))
x2 = float(input('Insira o valor de x2: '))
y2 = float(input('Insira o valor de y2: '))

distancia = ((x1 - x2)**2 + (y1 - y2)**2) ** 1/2

print(f'A distância entre os pontos é: {distancia}')