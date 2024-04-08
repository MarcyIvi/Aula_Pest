# Fatiamento (slicing) de string
# ex: range(inicio, fim, passo)
    
str = "Hoje é um bom dia"

# Fatiamento Simples
print(str[0]) # Primeiro Elemento 
print(str[1]) # Segundo Elemento 
print(str[-1]) # Último Elemento 
print(str[-2]) # Penúltimo Elemento

print("-" * 50)

# Fatiamento com intervalo
print(str[0:4])   #"Hoje"
print(str[10:13]) #"bom"
print(str[14:17]) #"dia"
print(str[14:])   #"dia"
print(str[:-1])   #"Hoje é um bom di"
print(str[0:])    #"Hoje é um bom dia"
print(str[:])     #"Hoje é um bom dia"

print("-" * 50)

#Fatiamento com passo 
print("Fatiamento com passo")
print(str[0::2])   #"Hj mbmda"
print(str[::2])    #"Hj mbmda"
print(str[-1::-1]) #"aid mob mu é ejoH"

print("-" * 50)
