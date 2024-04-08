str = "Thomaz"

# Acessando Elementos
print(f"Primeiro Elemento: {str[0]} ")
print(f"Primeiro Elemento: {str[1]} ")
print(f"Primeiro Elemento: {str[2]} ")
print(f"Primeiro Elemento: {str[-1]} ")
print(f"Primeiro Elemento: {str[-2]} ")
print(f"Primeiro Elemento: {str[-3]} ")

print("-" * 50)

# Tamanho da String
tamanho = len(str)
print(f"Tamanho da string: {tamanho} caracteres")

print("-" * 50)

# Acessar Todos os Elementos da String
print("Acessando todos os elemntos da string: ")

for i in range(tamanho):
     print(str[i])

for i in range(tamanho -1, -1, -1):
    print(str[i])

for i in range(-1, -tamanho -1, -1):
    print(str[i])

print("Acessando todos os elemntos da string: ")

for caractere in str: 
    print(caractere)

print("-" * 50)

