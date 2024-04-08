# 7. Crie uma função chamada invertendo_substrings que receba duas strings como entrada e 
# retorne uma nova string que consiste na primeira metade da segunda string invertida 
# concatenada com a segunda metade da primeira string também invertida. Veja o exemplo abaixo.

# Ex: invertendo_substrings("Python", "Programming")  deve retornar "gnimmtyP"

def invertendo_substrings(str1: str, str2: str):
    inver1 = str1[::-1]
    inver2 = str2[::-1]
    metade_1 = inver2[:len(str2)//2]
    metade_2 = inver1[len(str1)//2:]

    return metade_1 + metade_2

str1 = input('Digite uma string: ')
str2 = input('Digite uma string: ')

print(invertendo_substrings(str1, str2))
