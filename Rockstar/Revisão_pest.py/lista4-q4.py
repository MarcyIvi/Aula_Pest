n = int(input("Digite um número: "))
contador = 0
soma = 0 
for i in range(0, n + 1):
    soma += i
    contador += 1

media = soma/contador 
print(media)