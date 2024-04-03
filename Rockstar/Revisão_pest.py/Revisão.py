# 05/02/24

nome = input("Qual é seu nome ?")
idade = input("Qual é sua idade ?") 
# É necessário do int para dizer que idade é um número inteiro 
# Se não por nada a idade vira uma string

dobro_idade = idade * 2

print(nome)
print(f"Daqui a {idade} anos você terá {dobro_idade} anos.")