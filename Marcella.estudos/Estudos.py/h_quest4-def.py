def fatorial(num : int):
    for i in range(1, num + 1):
        f *=i

    return f




def comb(bino : int):
    global num
 


num = int(input('digite um número: '))

while num < 0  :
    num = int(input('digite um número: '))

res = fatorial(num)
print('o fatorial é :', res)

bino = int(input('digite um número para binominal: '))

while bino < 0:
    bino = int(input('digite um número para binominal: '))

res = comb(bino)
print(res)