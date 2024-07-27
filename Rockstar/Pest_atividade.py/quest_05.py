def maior_palavra(string1:str):
    lista_str = string1.split()
    tamanho_maior = 0
    palavra_maior = ''
    for i in lista_str:
        tamanho_atual = len(i)
        if tamanho_atual > tamanho_maior:
            tamanho_maior = tamanho_atual
            palavra_maior = i

    return palavra_maior

string1 = str(input('Digite uma string: '))
result = maior_palavra(string1)
print(result)

