def factorial(n : int ):
    fact = 1
    for n in range(1, n + 1):
        fact *= n 
    
    return fact
def comb(n : int, p : int):
    coe_b = factorial(n) / (factorial(p) * factorial(n - p))
    return coe_b

n = int(input('Digite um número: '))
p = int(input('Digite outro número: '))

while n < 0:
    n = int(input('Digite um outro número: '))
while p < 0:
    p = int(input('Digite um outro número: '))


resp = comb(n,p)
print(resp)
