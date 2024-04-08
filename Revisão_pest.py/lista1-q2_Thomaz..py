#05/02/24

quantidade = int(input('Digote a quantidade de livros:'))

preco_livro = 24.95

desconto = 40/100 # 0.4

preco_livro_com_desconto = 0.6 * preco_livro

valor_frete = 3 + 0.75 * (quantidade - 1)

valor_livros = quantidade * preco_livro_com_desconto

valor_total = valor_frete + valor_livros

print(f'O preço total é de: R$ {valor_total} sendo R$ {valor_livros} de livros e R$ {valor_frete} de transpórte.')