

class Conta:
    # self é a referência do endereço do objeto na memória
    #como defini o limite padrão como 1000.0, apenas é preciso informar como parametro caso seja um limite diferente
    def __init__(self, numero, titular, saldo, limite = 1000.0): #metodo constutor, executa a funcção automaticamente para definir os atributos
        print("Construindo objeto {}".format(self))
        self.numero = numero
        self.titual = titular
        self.saldo = saldo
        self.limite = limite
#Para chamar no console e criar um objeto: conta = Conta(1, "Eric Clapton", 0.0, 500.0)