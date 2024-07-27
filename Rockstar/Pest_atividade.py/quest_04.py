def remove_space(texto: str):
    lista_texto = texto.split()
    end_texto = " ".join(lista_texto)
    
    return end_texto

texto = str(input('Digite uma string: '))
result = remove_space(texto)
print(result)