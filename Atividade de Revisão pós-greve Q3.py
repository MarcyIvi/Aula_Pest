def palindromo(string: str):
    string = string.lower()
    string = string.replace(" ","")
    reverso = string[::-1]
    if reverso == string:
        return True
    else:
        return False

minha_str = str(input('Digite uma string: '))

if palindromo(minha_str):
    print(f'{}')
