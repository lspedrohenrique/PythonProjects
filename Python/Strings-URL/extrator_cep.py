import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

#Criando um padrão no Python, o metodo compile retorna um padrão, retorna o objeto pattern
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # '{}' são quantificadores
#Buscando em uma String se o padrão criado acima foi encontrado, retorna o objeto match(encontrou o padrão), retorna o match ou none caso não seja encontrado o padrão
busca = padrao.search(endereco)
if busca:
    cep = busca.group() #Retorna a substring encontrada no match acima
    print(cep)
