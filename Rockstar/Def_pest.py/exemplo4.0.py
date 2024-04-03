def funcao1():
    x = 10
    print(x)
    funcao2()
    print(x)

def funcao2():
    global x
    x = 20
    print(x)

x = 0
print(x)
funcao1()
print(x)
funcao2()
print(x)