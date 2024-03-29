# Ex: Programa para verificar se um número é primo

# Solicitar ao usuário um número para verificar se é primo
numero = int(input("Digite um número: "))

# Inicializar o contador de divisores
divisores = 0

# 29/01/24
# Inicializar o contador para iterar sobre os números
contador = 2

# Enquanto o contador for menor que o número
while contador <= numero:
    # Verificar se o número é divisível pelo contador atual
    if numero % contador == 0:
        # Se for divisível, incrementar o contador de divisores
        divisores += 1
    # Incrementar o contador
    contador += 1

# Verificar se o número de divisores é igual a zero
if divisores == 1:
    print(numero, "é primo!")
else:
    print(numero, "não é primo!")