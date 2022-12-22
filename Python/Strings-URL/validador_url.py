#https://www.bytebank.com.br/cambio <- padrão que sera representado na regex

import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url) #retorna none caso não encontre nada

if not match:
    raise ValueError('A URL não é valida.')

print('A URL é valida.')