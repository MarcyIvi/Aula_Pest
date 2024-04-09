nome_completo = str(input('Insira seu nome completo: ')).strip()
nome = nome_completo.split()

print('Seu primeiro nome é: ',nome[0])
print('Seu último nome é: ', nome[len(nome) - 1])