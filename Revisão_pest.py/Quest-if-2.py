# 19/02/24
nota = float(input("Insira a nota: "))

if nota >= 9:
    print('Parabéns! Você tirou A')
elif nota >= 7:
    print('Foi bem! Você tirou B')
elif nota >= 5 and nota < 7:
    print('Ok! Você tirou C') 
else: 
    print('Tem que melhorar! Você tirou D')