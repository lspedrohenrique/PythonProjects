

class Conta:
    # self é a referência do endereço do objeto na memória
    #como defini o limite padrão como 1000.0, apenas é preciso informar como parametro caso seja um limite diferente
    # Para chamar no console e criar um objeto: conta = Conta(1, "Eric Clapton", 0.0, 500.0)
    def __init__(self, numero, titular, saldo, limite = 1000.0): #metodo constutor, executa a função automaticamente para definir os atributos
        print("Construindo objeto {}".format(self))
        self.__numero = numero #Usamos o dois underline antes do nome do atributo para declarar um atributo privado
        self.__titual = titular
        self.__saldo = saldo
        self.__limite = limite
        #Encapsulado o acesso a atributos

    def extrato(self): #Metodo extrato
        print("Saldo {} do titular {}".format(self.__saldo, self.__titual))

    def deposita(self, valor): #Metodo deposita
        self.__saldo += valor

    def saca(self, valor): #Metodo saca
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor) #self também serve para chamar um método
        destino.deposita(valor)