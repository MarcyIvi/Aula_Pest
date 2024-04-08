#05/02/24

n = int(input('Digite um número: '))

unidade = n % 10
dezena  = (n//10) % 10
centena = (n//100) % 10 
milhar  = (n//1000) % 10 

soma = milhar + centena + dezena + unidade 

print(soma)