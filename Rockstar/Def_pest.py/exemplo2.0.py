def eh_primo(num:int):
    contador_de_divisores = 0

    for i in range(1, num + 1):
        if num % i == 0 :
            contador_de_divisores += 1

    if contador_de_divisores == 2:
        
        return True
    return False 

countador = 0 

while True:
    n = int(input('Digite um número: '))

    if eh_primo(n):
        