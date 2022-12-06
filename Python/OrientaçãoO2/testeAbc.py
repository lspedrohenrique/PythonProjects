from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)
#Sempre que você quiser garantir a implementação de alguns métodos,
#pode recorrer às classes já existentes em collections.abc e outros pacotes também.


#Classes abstratas são como se fossem moldes para suas classes filhas,
#eles impedem que você instancie uma classe filha sem implementar os métodos que você queria que sejam implementados.