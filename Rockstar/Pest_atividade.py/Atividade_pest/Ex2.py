# Criptografia Simples

# Este primeiro def vai começar a parte um do processo de criptogrfia, ele recebe a menssagem do usuário.

def cripto_tp(menssage: str):
    
    # Nesra parte coloquei todas as possibilidades de letras em TENIS-POLAR, as separei e dei slit. 
    # Transformando assim cada uma em uma váriavel.

        tenis_polar = 'TtEÉËÈÊẼeéëèêẽnNIÍÌÎĨÏiíìîĩïsS PpOÓÖÒÔÕoóöòôõlLAÁÀÂÃÄaáàâãärR'.split()
        
        t = tenis_polar[0]
        p = tenis_polar[1]
        
    # Servirá para armazenar a string com a primeira criptografia

        cripto1 = ''

    # O for vai passar por todos os caracteres de menssage e irá analisar se eles são de t ou de p, dessa forma
    # ele poderá pesquisar de qual indice é a letra, procurar no outro e colocar o caractere conrrespondente na 
    # cripto1 e assim por diante até ter a mensagem criptografada.

        for i in menssage:

            if i in t:
                letra = t.find(i)
                cripto1 += p[letra]

            elif i in p:
                letra = p.find(i)
                cripto1 += t[letra]

    # Se não estiver nem em t e nem em p irá armazenar o caractere de i em cripto1
            else: 
                cripto1 += i

    # Aqui ele vai retornar a menssagem criptografada anteriormente

        return cripto1

# Este def é a segunda parte da criptografia, onde ele vai trocar as vogais do que foi criptografado anteriormente.
# Recebe o resultado da cripto anterior.

def cripto_vogais(result : str):
        
    # Aqui coloquei todas as possibilidades de vogais, assim resultando em 12 cada vogal. Essa informação
    # será útil mais tarde.

        vogais = "AÁÄÀÂÃaáäàâãEÉËÈÊẼeéëèêẽIÍÏÌÎĨiíïìîĩOÓÖÒÔÕoóöòôõUÚÜÙÛŨuúüùûũAÁÄÀÂÃaáäàâã"
    
    # Fiz aqui um váriavel para armazenar a nova menssagem criptografada

        cripto2 = ''

    # Este for passará por todos os elementos de result e passrá para uma analise para descobrir se está em vogais. 
    # Se estiver ele irá pesquisa o indice de i e armazenará em letra. Depois vai somar a letra e 12 (Aqui a impor-
    # tância da informação anterior), assim dando a vogal corresponde a vogal i. Depois de tudo vai ser somado a cripto2.

        for i in result:
                
            if i in vogais:
                letra = vogais.find(i)
                cripto2 += vogais[letra + 12]

    # Quando não tiver a vogal somara a caractere de i a cripto2.

            else:
                cripto2 += i

    # Vai retonar o cripto2 já todo criptografado .

        return cripto2

# Aqui vai ser onde o usuário irá pôr sua menssagem.

menssage = str(input('Digite sua menssagem: '))

# Armazei o resultado da parte 1 da criptografia, para ser usado no segundo def.

result = cripto_tp(menssage)

# Aqui o resultado da segunda parte da criptografia sendo arazenado.
result = cripto_vogais(result)

# Aqui vai imprimir na tela o resultado 
print(result)

# Se vocÊ pôr Lápis na menssagem:
# Saída: Nóter

# Se você digitar a menssagem "Ataque ao amanhecer"
# Saída: Opoqau oi omolhucus