#URL sendo representada por uma String
url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

#Método para retornar o índice de uma String
indice_interrogacao = url.find('?')

#Fatiamento de Strings
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)