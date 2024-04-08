soma = 0 

for n in range(1, 100 + 1):
    contador = 0 

    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1

    if contador == 2:
        soma += n

print(soma)