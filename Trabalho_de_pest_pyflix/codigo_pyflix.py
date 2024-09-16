# Adicionar:
def adicionar(titulo: str, lista_de_filmes: list):

    # Cria uma lista para colocar os elementos do filme a ser adicionado
    filme = []
    titulo = remover_acento(titulo)
    filme.append(titulo)

    # Loop para adicionar o diretor e verificar a prença de caracteres especiais ou números
    while True:
        diretor = str(input("Qual é o diretor do filme ?  ")).lower().strip()

        # Chama a função remover acento e usa como argumento diretor
        diretor = remover_acento(diretor)

        if not verificar_caracteres(diretor):
            print("Erro! Nome de diretor inválido!")
        else:
            # Adiciona diretor a lista filme
            filme.append(diretor)
            break
    
    # Loop para adicionar o ano e verificar se ele é um número válido
    while True:
        ano = str(input(f"Qual o ano de lançamento do filme: {titulo.title()} ?  ")).strip()
        
        # Se o que for retornado do verificar_ano True ano seá adicionado a lista filme
        if verificar_ano(ano):
            filme.append(ano)
            break
    
    #Loop para adicionar o gênero do filme e verificar se ele tem algum caractere especial ou número
    while True:
        genero = str(input("Digite o gênero do filme: ")).lower().strip()

        # Chama a função remover_acento e tem como argumento o genero
        genero = remover_acento(genero)

        # Se o resultado da verificação for False ele avisa ao usuário que é inválido e retorna para início do loop
        if not verificar_caracteres(genero):
            print("Erro! Gênero inválido!")
        
        # Se o resultado da verificação for True, adicionara genero a lista filme
        else:
            filme.append(genero)
            break
    
   
    
    # Adiciona a lista filme a lista_de_filmes e escreve mais um filme no catálogo
    lista_de_filmes.append(filme)
    escrever(lista_de_filmes)
    
    # Confirma ao usuário que foi adicionado
    print("Filme adicionado ao catálogo! ")
  
# Listar:
def listar(lista_de_filmes: list):
     
     #Vai passar por cada lista ainhada de lista_ de _filmes, formatando e imprimindo na tela 
     tam = len(lista_de_filmes)
     for linha in range(tam):
        print("_" *50)
        print(f"Título: {lista_de_filmes[linha][0].title()}\nDiretor: {lista_de_filmes[linha][1].title()}\nAno de Lançamento: {lista_de_filmes[linha][2]}\nGênero: {lista_de_filmes[linha][3].capitalize()}")
        print("_" *50)

# Atualizar:
def atualizar(titulo: str, lista_de_filmes: list):
     
     # Faz uma verificação se o filme está no catálago
     for filme in lista_de_filmes:
          if filme[0] == titulo:
        
               while True:
                    # Loop com um menu de opções para serem realizadas
                    esc = str(input("""O que você deseja alterar ?
                    Digite [1] para alterar o título
                    Digite [2] para alterar o diretor
                    Digite [3] para alterar o ano
                    Digite [4] para alterar o gênero
                    Digite [0] para sair da seção atualização
                    : """)).strip()

                    # Altera o título
                    if esc == "1":
        
                        while True:
                            titulo = str(input("Digite o novo nome do filme: ")).lower().strip()

                            # Chama a função remover acento e tem como argumento titulo
                            titulo = remover_acento(titulo)

                            # Verifica se há um outro título com o mesmo nome, se não houver atualizara normalmente e salvara no catálago
                            if not verificar_filme(titulo, lista_de_filmes):
                                filme[0] = titulo
                                print("Título do filme atualizado!")
                                salvar(lista_de_filmes)
                                break
                            
                            # Se o titulo noameado para atualizar for igual ao um já existente ele vai falar que já tem e irá voltar para início do loop
                            else:  
                                print("Esse título já existe no catálogo! E não pode haver repetição de filmes!")
                                print("Coloque outro título")

                    # Altera o diretor
                    elif esc == "2":
                        while True:
                            diretor = str(input("Digite o nome do diretor atualizado: ")).lower().strip()

                            # Chama a função remover acento e tem como argumento diretor
                            diretor = remover_acento(diretor)

                            # Verifica a presença de caracteres estrnhos e números no diretor e mostra um mensagem de erro coltando para o início do loop
                            if not verificar_caracteres(diretor):
                                print("Erro! Nome de diretor inválido!")

                            # Se tudo estiver certo ele vai adicionar o diretor atualizado ao lista de filmes e vai salvar a alteração
                            else:
                                filme[1] = diretor
                                salvar(lista_de_filmes)
                                print("Diretor do filme atualizado")
                                break
                    
                    # Altera o ano
                    elif esc == "3":

                        while True:
                            ano = str(input("Digite o ano atualizado: ")).strip()
                                 
                            if verificar_ano(ano):
                                    filme[2] = str(ano)
                                    salvar(lista_de_filmes)
                                    print("Ano do filme atualizado!")
                                    break
                    
                    # Altera o genero
                    elif esc == "4":
                        while True:
                            genero = str(input("Digite o gênero do filme atualizado: ")).lower().strip()

                            # Chama a função remover acento e tem como argumento o genero
                            genero = remover_acento(genero)

                            # Verifica se p genero tem caracteres inválidos, pedindo para digitar novamente
                            if not verificar_caracteres(genero):
                                 print("Erro! Gênero inválido!")

                            # Se estiver tudo certo ele irá substituir na lista e vai salvar avisando para o usuário que está tudo certo
                            else:
                                filme[3] = genero
                                salvar(lista_de_filmes)
                                print('Genero do Filme atualizado!')
                                break
                    
                    # Sai do loop e retorna para o loop de opções principal
                    elif esc == "0":
                         print("Saindo...")
                         break
                    
                    # Mostra para o usuário que o que ele colocou deu erro e pede para digitar
                    else:
                        print("Erro digite novamente!")
                    
# Remover:
# Essa função irá remover o elemento do catálogo
def remover(lista_de_filmes):
     
     remover = str(input("Qual é o título que você deseja remover ?  ")).lower().strip()

     # Chama a função remover_acento com argumento remover
     remover = remover_acento(remover)
     
     for filme in lista_de_filmes:
          if filme[0] == remover:
               lista_de_filmes.remove(filme)
               salvar(lista_de_filmes)
               return True
     return False

# Essa função irá remover os acentos dos caracteres do elemento passado como argumento
def remover_acento(elemento: str):

    acentos = ['ã','á', 'à', 'â', 'ä', 'é', 'è', 'ê', 'ë', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 'ô', 'ö', 'õ','õ', 'ú', 'ù', 'û', 'ü', 'ç', 'ñ','´','`', '~','^',"'",'"',';','/','"\"','*']
    sem_acentos = ['a' ,'a', 'a', 'a', 'a', 'e', 'e', 'e', 'e', 'i', 'i', 'i', 'i', 'o', 'o', 'o', 'o', 'o','o', 'u', 'u', 'u', 'u', 'c', 'n','', '', '','',"",'','','','','']

    novo_elemento = ''

    # Irá passar por cada caractere do elemento
    for caractere in elemento:

        # Encontrado é constatado como falso até que ele passe pela vericação se o caractere é igual ao acento ele vai adiciona a letra conrrespondente ao novo_elemento, se o caractere não for igual ao acento o encontrado continua falso, assim adicionando o caractere a nova string
        encontrado = False
        for letra in range(len(acentos)):
            if caractere == acentos[letra]:
                novo_elemento += sem_acentos[letra]
                encontrado = True
                break
        
        if encontrado == False:
            novo_elemento += caractere
    
    return novo_elemento
         
# Buscar:

# Essa função vai buscar as informações do filme 
def buscar(lista_de_filmes: list):
    while True:
       # Menu de escolha para decidir como o usuário irá pesquisar o filme
       esc = str(input("""Você deseja realizar a pesquisa pelo ?
                    Digite [1] buscar pelo título
                    Digite [2] buscar pelo diretor
                    Digite [3] buscar pelo ano
                    Digite [4] buscar pelo gênero
                    Digite [0] para sair da seção de busca
                    : """)).strip()
       
       # Busca o título:
       if esc == '1':
            titulo = str(input("Qual título você gostaria de pesquisar ? ")).lower().strip()

            # Chama a função remover_acentos com o argumento sendo o título
            titulo = remover_acento(titulo)

            # Chama a função pesquisar para buscar o filme pelo título ou parte e dele, retorna a quantidade de títulos encontrados 
            quant_encontrados = pesquisar(esc, titulo, lista_de_filmes)
            
            # Verifica a quantidades de filmes encontrados
            if quant_encontrados == 0:

                # Confirma para o usuário não há elementos de acordo com a sua busca
                print('0 resultados pra busca...')
            else:
                # Mostra a quantidade de resultados da busca
                print(f'{quant_encontrados} resultados pra busca')
        
       # Busca pelo diretor, podendo buscar pelo nome dele ou parte do nome.
       elif esc == '2':

            diretor = str(input("Qual diretor você gostaria de pesquisar o filme? ")).lower().strip()
            
            #Chama a função remover_acento com argumento diretor 
            diretor = remover_acento(diretor)

            # Chama a função pesquisar para buscar o filme pelo nome do diretor ou parte e dele, retorna a quantidade de filmes encontrados com o nome buscado 
            quant_encontrados = pesquisar(esc, diretor, lista_de_filmes)

            # Verifica a quantidades de filmes encontrados
            if quant_encontrados == 0:

                # Confirma para o usuário não há elementos de acordo com a sua busca
                print('0 resultados pra busca...')

            else:
                # Mostra a quantidade de resultados da busca
                print(f'{quant_encontrados} resultados pra busca')


       elif esc == '3':
            
            # Loop para verificar_ano for True ele vai iterar sobre lista_de_filmes em busca de filmes com o mesmo ano imprimindo na tela o que encontrar
            while True:
                ano = str(input("Digite o ano a ser buscado: ")).strip().lower()

                cont = 0 
                if verificar_ano(ano):
                    for elemento in lista_de_filmes:
                        if ano in elemento[2]:
                            cont += 1
                            print("_" *50)
                            print(f"Título: {elemento[0].title()}\nDiretor: {elemento[1].title()}\nAno de Lançamento: {elemento[2]}\nGênero: {elemento[3].capitalize()}")
                            print("_" *50)
                
                # Se a quantidade de filmes encontrados for igual a 0 ele irá avisar ao usuário 
                if cont == 0:
                    print('0 resultados pra busca...')
                    break

                # Mostra quantos resultados encontrados ao usuário
                else:
                    print(f'{cont} resultados pra busca')
                    break
          
       elif esc == '4':
            
            genero = str(input("Qual título você gostaria de pesquisar ? ")).lower().strip()

            # Chama a função remover_acento como argumento o genero 
            genero = remover_acento(genero)

            # Chama a função pesquisar para buscar o filme pelo genero ou parte dele, retorna a quantidade de filmes encontrados com o genero buscado 
            quant_encontrados = pesquisar(esc, genero, lista_de_filmes)

             # Verifica a quantidades de filmes encontrados
            if quant_encontrados == 0:
                
                # Confirma para o usuário não há elementos de acordo com a sua busca
                print('0 resultados pra busca...')
            else:

                # Mostra a quantidade de resultados da busca
                print(f'{quant_encontrados} resultados pra busca')

        # Sai desse loop e volta para o principal
       elif esc == '0':
            print("Saindo da seção busca...")
            break
       
       # Mostra erro quando o usuário coloca uma opção inválida
       else:  
            print("Erro! Digite novamente!")

# Irá ver se o filme/diretor/genero está no catálogo. Se ele estiver irá mostrar os filmes com aquele nome ou parte do foi pesquisado e retona o valor de filmes que existem encontrados com a pesquisa.
def pesquisar(esc : str, obj_pesquisa: str, lista_de_filmes: list):
         
    cont = 0
    
    # Pesquisa o título
    if esc == '1':
        for elemento in lista_de_filmes:
            if obj_pesquisa in elemento[0]:
                cont += 1
                print("_" *50)
                print(f"Título: {elemento[0].title()}\nDiretor: {elemento[1].title()}\nAno de Lançamento: {elemento[2]}\nGênero: {elemento[3].capitalize()}")
                print("_" *50)
        return cont
    
    # Pesquisa o Diretor
    elif esc == '2':
        for elemento in lista_de_filmes:
                if obj_pesquisa in elemento[1]:
                    cont += 1
                    print("_" *50)
                    print(f"Título: {elemento[0].title()}\nDiretor: {elemento[1].title()}\nAno de Lançamento: {elemento[2]}\nGênero: {elemento[3].capitalize()}")
                    print("_" *50)
        return cont
    
    # Pesquisa o genero
    elif esc == '4':
        for elemento in lista_de_filmes:
                if obj_pesquisa in elemento[3]:
                    cont += 1
                    print("_" *50)
                    print(f"Título: {elemento[0].title()}\nDiretor: {elemento[1].title()}\nAno de Lançamento: {elemento[2]}\nGênero: {elemento[3].capitalize()}")
                    print("_" *50)
        return cont
    
# Verificações:

#Verifica se um filme está no nosso catálogo, retornado um booleano
def verificar_filme(titulo: str, lista_de_filmes : list):
     for filme in lista_de_filmes:
          if filme[0] == titulo:
               return True
     return False

#Verifica se o ano colocado pelo usuário contém outros caracteres além de números. Se for um número ele irá transforma para um número inteiro e depois irá verificar se o ano está dentro de um determinado intervalo de anos. 
def verificar_ano(ano : str):
     if not ano.isdigit():
          print("Só pode usar apenas números! Digite novamente!")
          return False
     else:
          ano_int = int(ano)
          if ano_int <= 2024 and ano_int >= 1888:
            return True
          
          else:
             print("Ano inválido digite novamente!")
             return False

# Verifica se o arquivo está vazio, lendo se há elementos no catálogo, retornando falso se não houver.
def verificar_arquivo(arquivo = "catalogo.txt"):

    with open(arquivo, "r") as banco_de_dados:
        conteudo = banco_de_dados.read()
        if conteudo == '':
            return False
        else:
            return True

# Verifica a presença de caracteres estranhos e números, permitindo apenas letras e espaços, além de retorna um booleano
def verificar_caracteres(elemento: str):

    for caractere in elemento:
        if caractere not in 'abcdefghijklmnopqrstuvwxyz ':
            return False
        
    return True


# Armazenar:

# Ao adicionar filmes você escreve novos filmes no catálogo sem substituir os antigos 
def escrever(lista_de_filmes : list):

    with open("catalogo.txt", "w") as catalogo:
        for filme in lista_de_filmes:
            catalogo.write(f"{filme[0]},{filme[1]},{filme[2]},{filme[3]}\n")

# Salva as alterações feitas durante o código, escrevendo por cima do que estava escrito antes, dessa forma substituindo os elementos antigos do catalogo e escrevdo as novas alterações no catálogo
def salvar(lista_de_filmes: list, arquivo = 'catalogo.txt'):

    with open(arquivo, "w") as banco_de_dados:
        for filmes in lista_de_filmes:
            filme = ",".join(filmes)
            banco_de_dados.write(filme + "\n")

# Essa função transforma os elementos no catálogo de filmes em elementos da nossa lista de filme, adicionado eles a lista e retorna a lista de filme carregada
def carregar(lista_de_filmes : list, arquivo = 'catalogo.txt'):

    with open(arquivo, "r") as banco_de_dados:
        for filmes in banco_de_dados:
            filme = filmes.strip().split(",")
            lista_de_filmes.append(filme)

    return lista_de_filmes

# Cria a lista de filme 
lista_de_filmes = []

# Verifica se há filmes em nosso banco de dados e retorna True se houver filmes nele 
if verificar_arquivo("catalogo.txt") == True:
    # Carrega os filmes do catálogo na nossa lista de filmes
    lista_de_filmes = carregar(lista_de_filmes)

# loop para iniciar o programa pyflix
while True:
    #Mostra as opções
    print('''Olá! Seja bem-vindo a PyFlix!
O que você deseja fazer com o nosso catálogo ?
      - Digite [ad] para adicionar filmes
      - Digite [li] para listar filmes
      - Digite [at] para atualizar filmes
      - Digite [re] para remover filmes
      - Digite [bu] para buscar filmes
      - Digite [sa] para sair do noso programa''')

    esc = input("Você deseja fazer: ").lower().strip()

    # Para adicionar um filme: 
    if esc == "ad":  
            
            # Loop o usuário adicionar um filme
            while True:
                titulo = str(input("Qual filme você gostaria de adicionar?  ")).lower().strip()

                #Chama a função para remover os acentos do titulo 
                remover_acento(titulo)
                
                # Verifica se o titulo já existe no catálogo, se não existir adiciona normalmente
                if not verificar_filme(titulo, lista_de_filmes):
                    adicionar(titulo, lista_de_filmes)
                    break  

                # Confirma pro usuário que o filme já existe e irá voltar para o início do loop pedindo novamente o título
                else:    
                    print("Filme já exixtente na plataforma")
                    print("Digite novamente!")       

    # Para listar:
    elif esc == "li":
            
            # Verifica se há elementos na lista para serem listados
            if lista_de_filmes == []:
                print("Não há filmes no catálogo")

            # Se tiver elementos na lista ele ira chamar a função listar para mostrar de forma formatada os elementos da lista/catálogo
            else:
                listar(lista_de_filmes)

    elif esc == "at":
            
            # Verifica se há elementos no catálogo para serem atualizados
            if lista_de_filmes != []:
                 while True:
                    titulo = str(input("Digite qual título você quer atualizar: ")).lower()
                    titulo = remover_acento(titulo)
                    
                    # Verificar se o filme existe no catálogo para atualizar
                    if not verificar_filme(titulo, lista_de_filmes):
                        print("Filme inexistente no catálogo para ser atualizado!")
                    
                    # Depois das verificações se o filme estiver no catálogo ele vai ser atualizado
                    else:
                        atualizar(titulo, lista_de_filmes)
                        break  
            
            else:
                 # Confirma pro usuário que não há filmes no catálogo para serem atualizados
                 print("Não há filmes no catálogo para serem atualizados!")
                                      
    # Para remover algum filme
    elif esc == "re":

        # Verifica se há elementos no catálogo para serem remvidos
        if lista_de_filmes == []:
             print("Não há nada no catálogo para ser removido!")

        # Se houver ele vai iniciar um loop para verificar se o filme existe no catálogo e removê-lo
        else:
            while True:
                if remover(lista_de_filmes):
                    print("Filme removido!")
                    break

                # Se não existir no catálogo ele confirma que não há esse filme para ser removido   
                else:
                    print("Esse filme não existe no catálogo para ser removido")

    # Para buscar algum filme
    elif esc == "bu":
         
         #Verifica se há filmes no catálogo para serem buscados
         if lista_de_filmes == []:
              print("Catálogo Vazio para busca de filmes!")
         
         # Chama a função para buscar o filme
         else:
              buscar(lista_de_filmes)
    
    # Opção de saída do programa pyflix
    elif esc == "sa":
         print("Saindo...")
         # Salva os filmes no catalogo.txt(nosso arquivo)
         salvar(lista_de_filmes)
         break
    
    # Se a pessoa não colocar uma das opções citadas no menu, vai avisar ao usuário que deu erro e vai pedir para digitar novamente
    else:
         print("Erro! Opção inválida! Tente novamente!")