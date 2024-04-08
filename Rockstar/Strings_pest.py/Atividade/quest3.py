# Escreva uma função chamada reverter que aceite uma string como entrada e retorne a string revertida.

def reverter(string: str):
    x = ''
    tamanho = len(nova_string)
    for i in range(-1, -tamanho -1, -1):
        x += string[i]
    print(x)

    # fatiamento = string[-1::-1]
    # return fatiamento



nova_string = input("Digite uma string: ")
reverter(nova_string)

# print(reverter(nova_string))