# Um aluno tem cinco notas e deseja calcular a média 
# aritmética dele

notas = [10, 7.5, 3.6, 8.1, 5]

soma = 0
for nota in notas:
    soma += nota

media = soma/len(notas)
print(media)

# Leia 5 notas do usuário, coloque-os numa lista e calcule a média dessas notas.
# OBS: Só calcule a média depois que as notas estiverem na lista!

notas = [0,0,0,0,0]

for i in range(5):
    notas[i] = float(input(f"Digite a nota { i + 1 }:"))
    soma += nota[i]

print(soma / len(notas))