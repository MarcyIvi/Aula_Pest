# 1.Crie um a lista de frutas quaisquer. Em seguida,
# peça ao usuário para inserir o niome da fruta e 
# e verifique se essa fruta está na lista. Exiba 
# uma mensagem informando se a fruta está ou não.

# frutas = ['maçã', 'cereja', 'uva', 'banana', 'kiwii', 'laranja', 'abacaxi']

# nome_fruta = str(input('Digite uma fruta: '))

# if nome_fruta in frutas:
#     print('Essa fruta existe nesse MUNDO!')
# else:
#     print('NÃO EXISTE ESSA FRUTA NESSE NUNDO, SEU ALIEN!')

# print(' ')

# 2. Escreva um programa que encontre o maior  
# número em uma lista de números inteiros. Use o loop 
# FOR para percorrer a lista.

# numeros = [10, 20, -6, 200, 11.7, 5, 14]

# maior_numero = -99999

# for elementos in numeros:

#     if elementos > maior_numero:
#         maior_numero = elementos

# print(maior_numero)


# 3. Refaça o programa anterior usando funções. Sua 
# função deve receber uma lista e retornar o maior 
# número da lista.

def retorna_maior(L : list):
    
    maior_numero = L[0]

    for item  in L:
        if item > maior_numero:
         maior_numero = item

    return print(maior_numero)

Lista_de_numeros = [13, 200, 90, 1090, -11]
retorna_maior