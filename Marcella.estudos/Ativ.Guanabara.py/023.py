###n = str(input('Digite um número de 0 a 9999: '))

#unidade  = n[3]
#dezena   = n[2]
#centena  = n[1]
#milhar   = n[0]

#print(f'''Seu número é: {n}
#unidade = {unidade}
#dezena  = {dezena}
#centena = {centena}
#milhar  = {milhar} ''')

# O problema do de cima é que só funciona com 4 números

num = int(input('Insira um número: '))
u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''Seu número é: {num}
unidade = {u}
dezena  = {d}
centena = {c}
milhar  = {m} ''')