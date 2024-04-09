frase = str(input('Digite uma frase: ')).lower().strip()

print(frase.count('a'),'está é a quantidade de a na sua frase.')
print('A primeira letra a apareceu nesta posição: ',frase.find('a') + 1 )
print('A útilma letra apareceu nesta posição: ', frase.rfind('a') +1)

