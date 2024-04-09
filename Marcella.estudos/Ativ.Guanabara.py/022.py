nome_completo = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é: ',nome_completo.upper())
print('Seu nome em minúsculas é: ',nome_completo.lower())
print('Seu nome tem ao todo ',len(nome_completo) - nome_completo.count(' '),' letras')
#print('Seu primeiro nome tem ',nome_completo.find(' '))
separa = nome_completo.split()
print(f'Seu primeiro nom é {separa[0]} e ele tem {len(separa[0])}')
