- Utilização:

PyFlix é um gerenciador de catálogo de filmes desenvolvido em Python. Este programa permite aos usuários adicionar, listar, atualizar, remover e buscar filmes em um catálogo, com dados armazenados em um arquivo de texto chamado catalogo.txt.
Ao iniciar o programa, você verá um menu com as opções sitadas anteriormente:

[ad] Adicionar filme
[li] Listar filmes
[at] Atualizar filme
[re] Remover filme
[bu] Buscar filme
[sa] Sair do programa

* Adicionar Filme:
Permite com que o usuário digite o título do filme e forneça informações adicionais como diretor, ano e gênero. O filme será adicionado ao catálogo se o título ainda não existir.

* Listar Filmes:
Mostra todos os filmes no catálogo em formato detalhado.

* Atualizar Filme
Permite com que o usuário digite um filme existente e consiga alterar seu título, diretor, ano ou gênero.

* Remover Filme
Permite com que o usuário digite o título do filme para removê-lo do catálogo.

* Buscar Filme
Permite com que o usuário busque filmes por título, diretor, ano ou gênero. O programa exibirá todos os filmes que correspondem à sua pesquisa.

* Arquivo de Dados
O catálogo de filmes é armazenado em um arquivo chamado catalogo.txt. Cada linha representa um filme com o seguinte formato:
Título, Diretor, Ano, Gênero


- Funções Principais:

A seguir, estão as funções principais realizadas no código com suas determinadas funcinalidades:

adicionar(titulo: str, lista_de_filmes: list): 
Adiciona um filme à lista de filmes.

listar(lista_de_filmes: list): 
Exibe todos os filmes na lista.

atualizar(titulo: str, lista_de_filmes: list): 
Atualiza os dados de um filme existente.

remover(lista_de_filmes: list): 
Remove um filme da lista.

buscar(lista_de_filmes: list): 
Busca filmes por critérios especificados.

remover_acento(elemento: str): 
Remove acentos de caracteres.

verificar_caracteres(elemento: str): 
Verifica se a string contém apenas caracteres válidos.

verificar_ano(ano: str): 
Verifica se o ano é válido.

escrever(lista_de_filmes: list): 
Salva a lista de filmes no arquivo.

salvar(lista_de_filmes: list): 
Atualiza o arquivo com as últimas alterações.

carregar(lista_de_filmes: list): 
Carrega filmes do arquivo para a lista.