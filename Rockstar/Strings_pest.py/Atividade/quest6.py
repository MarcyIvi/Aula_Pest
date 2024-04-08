# 6. Implemente uma função chamada letras_alternadas que receba uma string como entrada e retorne uma nova 
# string contendo apenas os caracteres nos índices pares da string original.

def letras_alternadas(str1: str):
    new_str = str1[::2]

    return new_str

str1 = input('Digite uma string: ')
print(letras_alternadas(str1))