# Capitalize

def meu_capitalize(str1 : str):
    mini = 'abcdefghijklmnopqrstuvwxyz'
    gran = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    tamanho_str = len(str1)
    ind = 0
    for i in range(26):
        if str1[0] == mini[i]:
            ind += i
    return gran[ind] + str1[1:]

str1 = input('Digite uma string: ')
print(meu_capitalize(str1))         