#05/02/24

hora_do_relogio = int(input('Digite a hora do relógio: '))
dispertar = int(input('Insira depois de qunatas horas você quer acordar: '))

hora = hora_do_relogio + dispertar
acordar = dispertar % 24

print(f'Você irá acordar às {acordar}')