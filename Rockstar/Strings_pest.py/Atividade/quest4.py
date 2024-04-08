# Crie uma função chamada saltos que receba uma string e um número inteiro positivo como entrada, 
# representando o tamanho do salto, e retorne uma nova string contendo apenas os caracteres da 
# string original que estão nos índices múltiplos do tamanho do salto.

# Ex: saltos("Python Programming", 3)  deve retornar "Ph oai”

def saltos(string: str, n_salto: int ):
    while n_salto < 0:
        n_salto= int(input("Digite um número: "))

    tex_pulo = string[::n_salto]
    return tex_pulo      

nova_string = input("Digite um string: ")
n_salto = int(input("Digite um número: "))
print(saltos(nova_string, n_salto))