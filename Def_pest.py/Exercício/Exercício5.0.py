def conversor_moedas(real : float, taxa: float):
    dolar = real / taxa
    return dolar 

real = float(input('Digite o valor em BRL: '))
taxa = float(input('Insira o valor da taxa do câmbio: '))

res = conversor_moedas(real, taxa)
print(f'O valor em dólar será: {res}')