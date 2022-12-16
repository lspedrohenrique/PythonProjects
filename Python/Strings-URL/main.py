#URL sendo representada por uma String
url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitização da URL
url = url.strip() # Poderia ter usado o replace também

#Validação da URL
if url == "":
    raise ValueError('A URL está vazia') #Retornando um erro no terminal do tipo valor


#Método para retornar o índice de uma String
indice_interrogacao = url.find('?')

#Fatiamento de Strings
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

paramentro_busca = 'quantidade'
indice_parametro = url_parametros.find(paramentro_busca)
indice_valor = indice_parametro + len(paramentro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor) #a partir de qual posição você quer encontrar algo
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
    print(valor)
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)