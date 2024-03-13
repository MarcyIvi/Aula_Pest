def eh_par(n : int):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número: '))
res = eh_par(n)
print(res)