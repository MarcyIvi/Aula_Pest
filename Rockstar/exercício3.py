# 1.Crie um a lista de frutas quaisquer. Em seguida,
# peça ao usuário para inserir o niome da fruta e 
# e verifique se essa fruta está na lista. Exiba 
# uma mensagem informando se a fruta está ou não.

frutas = ['maçã', 'cereja', 'uva', 'banana', 'kiwii', 'laranja', 'abacaxi']

nome_fruta = str(input('Digite uma fruta: '))

if nome_fruta in frutas:
    print('Essa fruta existe nesse MUNDO!')
else:
    print('NÃO EXISTE NESSE NUNDO SEU ALIEN!')

print(' ')

# 2. Escreva um programa que encontre o maior  
# número em uma lista de números inteiros. Use o loop 
# FOR para percorrer a lista.

numeros = [10, 20, 6, 200, 11, 5, 14]

for elementos in numeros:
    

# 3. Refaça o programa anterior usando funções. Sua 
# função deve receber uma lista e retornar o maior 
# número da lista.