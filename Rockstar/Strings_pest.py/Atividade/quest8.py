# 8. Escreva uma função chamada intercalar_letras que aceite duas strings como entrada e 
# retorne uma nova string contendo as letras intercaladas das duas strings, ou seja, 
# a primeira letra da primeira string, a primeira letra da segunda string, a segunda 
# letra da primeira string e assim por diante.

# Ex: intercalar_letras("Olá", "Mundo!") deve retornar "OMluándo!”

def intercalar_letras(str1: str, str2: str):
    str1_t = len(str1)
    str2_t = len(str2)
    new_str = ''
    
    if str2_t >= str1_t:
        menor = str1_t
        maior = str2_t
        for i in range(menor):
            new_str += str1[i] + str2[i]
        if not str2_t == str1_t:
            for j in range(i + 1, maior):
                new_str += str2[j]
    
    else:
        menor = str2_t
        maior = str1_t
        for i in range(menor):
            new_str += str1[i] + str2[i]
        for j in range(i +  1, maior):
            new_str += str1[j]

    return new_str

str1 = input('Digite uma string: ')
str2 = input('Digite uma string: ')

print(intercalar_letras(str1, str2))