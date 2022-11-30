class Contador():
    def __init__(self): #construtor dos atributos do objeto
        self.saldo_contador = 0

    def contar(self): #Metodo contar
        self.saldo_contador += 1
        print(self.saldo_contador)