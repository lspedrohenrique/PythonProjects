serio = range(0, 9)


for i in serio:
    print(serio[i])

valores = ("a","b","c","d","e") #tupla

lista = [4,3,2,1] #mutavel
lista.append(99)

tuple = (4,3,2,1) #imutavel
print(tuple)

colecao = {11122233344, 22233344455, 33344455566} #set
colecao.add(44455566677) #vai adicionar pois não existe ainda // para adicionar um elemento a um set devemos chamar a função add
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe! // não da erro, o Python só ignora
print(colecao)


instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30} #dictionary também pe aberto com chaves, sempre acompanhado de um valor // chave : valor
print(instrutores["Marcos"]) #Sairá 30

inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0] #List Comprehensions

arquivo = open('nome.txt', 'w')