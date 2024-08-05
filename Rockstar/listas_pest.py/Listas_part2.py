# Adicionando elementos na lista - APPEND

L = [3, 4, 10, 4, 3, 8, 5, 0]

tamanho_da_lista = len(L)

print(f"Tamanho da lista ANTES do append: {tamanho_da_lista}")
L.append('garrafa')

tamanho_da_lista = len(L)

print(f"Tamanho da lista DEPOIS do append: {tamanho_da_lista}")
print(L)

# Crie uma função que receba uma lista e um elemento sozinho. 
# Adicione esse elemento ao final dessa lista e retorne essa 
# lista com esse novo elemento.

def add_elemento(Lista  : list, elemento):
    Lista.append(elemento)
    return Lista


Lista = ['a', 'b', 'c']
print(f'Lista antes: {Lista}')
print(f"Lista depois: {add_elemento(Lista, 4)}")


# Adicionado elementos na Lista - INSERT
# Usado em posições específicas

L = [3, 4, 10, 4, 3, 8, 5, 0]

tamanho = len(L)
print(f"Tamanho ANTES: {tamanho}")

L.insert(2, 'a')
print(L)
tamanho = len(L)
print(f"tamanho DEPOIS: {tamanho}")

# Removendo elementos de uma lista - REMOVE

L = [3, 4, 10, 4, 3, 8, 5, 0]

print(L)
L.remove(10)
print(L)

# Faça uma função para receber uma lista e um elemento. Caso esse elemeento exista dentro da lista, remova-o.
# Caso não exista , adicione ao final da lista.
# Sus função não deve retornar nada.

def add_remover(Lista : list, elemento):
    
    if elemento in Lista:
        Lista.remove(elemento)
    else:
        Lista.append(elemento)

Lista = list()

add_remover(Lista, input('Digite alguma coisa: '))
print(Lista)

add_remover(Lista, input('Digite alguma coisa: '))
print(Lista)

add_remover(Lista, input('Digite alguma coisa: '))
print(Lista)

add_remover(Lista, input('Digite alguma coisa: '))
print(Lista)

# Removendo elementos da lista - DEL

L = [3, 4, 10, 4, 3, 8, 5, 0]
print(f"antes: {L}")

del L[5] #L.remove(8)
print(f"depois: {L}")

