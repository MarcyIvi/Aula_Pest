def calculadora(oper: int, num1: float, num2: float):
    if oper == 1:
        resul = num1 + num2
    elif oper == 2:
        resul = num1 - num2
    elif oper == 3:
        resul = num1 * num2
    elif oper == 4:
        resul = num1 / num2

    return resul

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
oper = int(input('''Olá escolha a operação:
Soma -> [1]
Subtração -> [2]
Multiplicação -> [3]
Divisão -> [4] 
: '''))

res = calculadora(oper, num1, num2)
print(res)
