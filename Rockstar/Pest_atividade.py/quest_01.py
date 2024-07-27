def inverter_str(string:str):
    tam = len(string)
    rever_str = string[-1:-tam -1:-1]
    return rever_str


string = str(input('Digite uma string: '))
reverso = inverter_str(string)
print(f'Sua string ao contrario é:\n{reverso}')
