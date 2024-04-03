#05/02/24

hora_atual = float(input('Insira a hora atual: '))
tempo_de_espera = float(input('Insira o tempo de espera: '))

a = (hora_atual + tempo_de_espera) 
alarme = a % 24

print(f'O alarme irá tocar às {alarme}')