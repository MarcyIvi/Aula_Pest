# Escreva uma função em Python chamada primeiro_e_ultimo que receba uma string como 
# entrada e retorne uma nova string contendo apenas o primeiro e o último caractere 
# da string original.

def primeiro_e_ultimo(string: str):
    # primeiro_caractere = string[0]
    # tamanho = len(string)
    # ultimo_caractere = string[-1]
    # res = primeiro_caractere + ultimo_caractere
    # return res 
    return string[0] + string[-1]

nova_string = input("Digite uma string: ")
print(primeiro_e_ultimo(nova_string))