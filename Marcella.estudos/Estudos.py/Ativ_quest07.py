from random import randint

def jogo_de_adivinhacao():

    aleatorio = randint(1, 100)
    contador = 0
    n = int(input('Iai ? Qual é seu palpite? Olha que ele tem quer ser de 1 a 100. '))
    
    contador += 1 
    while True:
        while n > 100:
             n = int(input('Eu lhe disse que era entr 1 e 100, tente de novo:  '))
             contador += 1
        while n < 1:
             n = int(input('Eu lhe disse que era entr 1 e 100, tente de novo:  '))
             contador += 1

        if n > aleatorio:
            n = int(input('O número é menor...que pena, tente novamente: '))
            contador += 1
            
        elif n < aleatorio:
            n = int(input('O número é maior...que pena, tenta novamente:  '))
            contador += 1

        else:
            print(f'Que surpreendente! Você ganhou!!! Voce tentou: {contador} vezes, o número era {aleatorio} e seu era {n}')
            break
jogo_de_adivinhacao()