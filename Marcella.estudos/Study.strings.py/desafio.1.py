# Lower 

def meu_lower(str1: str):
    mini = 'abcdefghijklmnopqrstuvwxyz'
    gran = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tamanho_str  = len(str1)
    nova_str = ''
    for i in range(tamanho_str):
        for g in range(26):
            if str1[i] == gran[g]:
                nova_str += mini[g]
    
    return nova_str
str1 = input('Digite uma string: ')
print(meu_lower(str1))