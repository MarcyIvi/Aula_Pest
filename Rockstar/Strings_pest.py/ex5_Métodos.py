# Metétodos de Strings
# --------------------
# Método = funções
# --------------------
# com/ sem retorno
# com/ sem paramêtro

# 1. capiatalize() - Retorna a string com a primeira letra em caixa alta

def funcao(palavra : str):
    palavra.capitalize() 
    print(palavra.capitalize())

funcao("Abacaxi")

# 2. lower() - Converte strings para minúsculos

nome = input("Digite seu nome: ").lower()

print(nome)
print(nome.upper())

# 3. upper() - Converte strings para MAIÚSCULO

nome = input("Digite seu nome: ").upper()

print(nome)
print(nome.lower())

# 4. split() - Divide a string com base em um separador e retorna uma lista

frase = "Hoje é um bom dia"

lista_frase = frase.split() # separador: espaço ' ' 
print(lista_frase)
lista_frase = frase.split('m') # separador: 'm'
print(lista_frase)

# Sem argumento - [Hoje, é, um, bom, dia]
# Com argumento que existe na string - [Hoje é u, bo, dia]
# COm argumento que não existe na string - [Hoje é um bom dia]

# 5. join() - Une elementos de uma lista usando uma string como "separador"

frase = "Hoje é um bom dia"

lista_frase = frase.split('m') 
print(lista_frase)

palavra = "#"
print(palavra.join(lista_frase))

# 6. replace() - Substitui um determindado trecho da string por outro 

nome = input("Digite seu nome: ").upper()

novo_nome = nome.replace('ABACAXI', 'MELANCIA')
novo_nome = nome.replace('A', '4')
novo_nome = novo_nome.replace('E', '3')
novo_nome = novo_nome.replace('I', '1')
novo_nome = novo_nome.replace('O', '0')
print(novo_nome)

# 7. find() - Retorna o índice da primeira ocorrência até um determinado valor.

frase = "Hoje é um bom dia"

print(frase.find('m')) # 8
print(frase.find('x')) # -1

# 8. index() - Mesma coisa do find() mas da erro se não existir

frase = "Hoje é um bom dia"

print(frase.index('m')) # 8
print(frase.index('x')) # ERRO!

# 9. count() - Conta o número de ocorrências de um determindado valor numa string

frase = "Hoje é um bom dia"

print(frase.count('M'))

# 10. islower() - Retorna True se a string for minúscula 

frase = "hoje"
if frase.islower() == True: 
    print("Tudo minúsculo")
else:
    print("NEM Tudo é minúsculo")