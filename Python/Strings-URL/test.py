class Minha():
    def __init__(self, string):
        self.string = string

    def retorna_string(self):
        return self.string

    def retorna_string_cortada(self):
        return self.retorna_string()[10:]

teste = Minha("Pedro Henrique Leite de Souza")

print(teste.retorna_string())
print(teste.retorna_string_cortada())