# Exemplo de Listas:

L = ["a", "bom", 100, 5.5, " "]

# Lista vazia

L1 = []
L2 = list()

# Acessando elementos 

print(L[0])
print(L[3])
#print(L(5)) # Erro de indice

# Modificando elementos

L[0] = 'x'
print(L)

str1  = 'ovo'
str2  = 'ana'
str3  =  str1
print(str3) # ana

str1 = 'ana'
str2 = 'ovo'
print(str3) # ovo

L1 = ['ovo']
L2 = ['ana']
L3 = L1
print(L3) # ['ovo']

L2 = ['ovo']
L1 = ['ana']
print(L3) # ['ovo']

# Copiando elementos

L1 = [1, 2, 3]
L2 = [4, 5, 6]
LC = L1
print(LC)

print(f"L1: {L1}")
print(f"LC: {LC}")

L1[0] = 'x'
LC[0] = 'y'

print(f"L1: {L1}")
print(f"LC: {LC}")

COPIA = L1[:]
L1[0] ='w'
COPIA[0] = 'z'

# Fatiamneto [slicing]

L = ['a', 1, 'b', 2, 'c', 3, 'd', 4]

# L[ inicio : final : passo ]

L[::2]  # ['a', 'b', 'c', 'd']
L[1::2] # [1,2,3,4]

#  Percorrendo Lista
L = ['a', 1, 'b', 2, 'c', 3, 'd', 4]

tamanho_da_lista = len(L)

for i in range(tamanho_da_lista):
    print(L[i])

for elemento in L:
    print(elemento)


