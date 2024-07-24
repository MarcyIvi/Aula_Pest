def contar_vogais(strin: str):
    
    cont = 0
    vogais = 'AEIOUaeiouÁÉÍÓÚáéíóúàèìòùÀÈÌÒÙÂÊÎÔÛâêîôûÃÕãõÄËÏÖÜäëïöü'
    
    for s in strin:
        if s in vogais:
            cont += 1

    return cont

strin = str(input('Digite uma string: '))
quant_v = contar_vogais(strin)


print(f'A quantidade de vogais é: {quant_v}')