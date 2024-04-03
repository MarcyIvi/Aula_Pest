# Crie uma função chamada intervalo que receba uma string e dois índices (int) 
# como parâmetros de entrada e retorne a substring que está entre esses dois índices, 
# incluindo o caractere no primeiro índice, mas excluindo o caractere no último índice.
    
# *Ex: intervalo (”Python”, 1, 4) deve retornar a substring “yth”.

def intervalo(string: str, ind_1: int, ind_2: int):
    return string[ind_1 : ind_2]

nova_string = input("Digite uma string: ")
ind_1 = int(input('Digite um número: '))
ind_2 = int(input("Digite outro número: "))

print("O intervalo é:", intervalo(nova_string,ind_1,ind_2) )
