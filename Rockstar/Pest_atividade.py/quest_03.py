def palindromo(string: str):
    string = string.lower()
    string = string.replace(" ","")
    reverso = string[::-1]
    if reverso == string:
        return True
    else:
        return False

string = str(input('Digite uma string: '))
result = palindromo(string)
if result == True:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')