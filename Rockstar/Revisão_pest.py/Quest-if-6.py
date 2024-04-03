# 19/02/24
# 19/02/24

num = int(input('Digite um número de 5 digitos: '))

unidade = num % 10
dezena = (num//10) % 10
dezena_mi = (num//100000) % 10
milhar = (num//1000) % 10
centena = (num//100) % 10

if (unidade == dezena or unidade == centena or unidade == milhar) or (dezena == centena or dezena == milhar or dezena == dezena_mi) or (centena == milhar or centena == dezena_mi) or (milhar == dezena_mi):
    print("Têm números repetidos")
else:
    print("Não têm números repetidos")