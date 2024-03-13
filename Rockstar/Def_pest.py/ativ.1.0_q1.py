def calculadora(n1 : float , n2 : float, opera : str):
    if opera == 'sum':
        res = n1 + n2 

    elif opera == 'sub':
        res = n1 - n2

    elif opera == 'mult':
        res = n1 * n2 

    
    elif opera == 'divi':
        res = n1 / n2

    return res

n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))

opera = input('''Olá seja bem-vindo(a) a calculadora!
Escolha a operação:
Soma          [sum]
Subtração     [sub]
Multiplicação [mult]
Divisão       [divi]
Por favor digite o número da operação desejada: ''')

resposta = calculadora(n1, n2, opera)

print(resposta)


