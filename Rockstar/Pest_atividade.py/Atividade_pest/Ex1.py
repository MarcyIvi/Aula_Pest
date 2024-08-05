# Validador de nomes de usuário

def validador_nome(nome : str):

    # Bloco que vai analisar o tamanho do nome de usuário

    tam = len(nome)
    valida = True

    if tam < 6 or tam > 15:
        valida = False
    else:
        valida = True
    
    # Bloco que vai analisar os caracteres do nome de usuário

    for i in nome: # O for vai passar 
        if i in '₢, ¹!²@³#£$¢%¬&*()-+=§:;[]{"''´}^~`.><|\/?°ªºôÔõÕâÃÂãÊêÎîûÛÜÖÄÏËäëïöüÀÈÌÒÙÁÉÍÓÚáéíóúàèìòù':
            valida = False
    
    # Irá retornar True ou False
    return valida 

# Pedido do nome de usuário, tambémm conhecido como nossa entrada

nome = str(input('Insira um nome de usário: '))

# Result vai mostrar o valor retornado da função

result = validador_nome(nome)

# While vai mostrar para o usuáio se seu nome é válido, 
# se não for pedirá novamente para que insira

while result == False:
    print('Nome de usuário inváido! Tente novamente!')
    nome = str(input('Insira um nome de usário: '))
    result = validador_nome(nome)

# Mostra ao usuário a confirmação de aprovação do nome de usuário

print('Nome de usuário aprovado!')