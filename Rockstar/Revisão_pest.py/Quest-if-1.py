# 19/02/24
num = int(input("Digite um número para verificar: "))

if num % 2 == 0 and num != 0 :
    pares = num
    #print(f"O número {pares} é par")
elif num == 0:
    print("0 não é ímpar nem par!")
else:
    impares = num
    #print(f"O número {impares} é ímpar")