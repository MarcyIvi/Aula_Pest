# Escreva uma função chamada concatenar_fatiar que aceite duas strings como entrada e 
# retorne uma nova string que consiste nos três primeiros caracteres da primeira string
# concatenados com os três últimos caracteres da segunda string.

#  concatenar_fatiar("Python", "Programming")  deve retornar "Pyting”

def concatenar_fatiar(text_1: str, text_2: str):
    tam = len(text_2)
    fat_1 = text_1[0:3]
    fat_2 = text_2[-3:tam]
    juncao = fat_1 + fat_2

    return juncao

text_1 = input("Digite uma string: ")
text_2 = input("Digite outra string: ")
print(concatenar_fatiar(text_1, text_2))