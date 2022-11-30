class Programa:
    def __init__(self, ano, genero):
        self.ano = ano
        self.genero = genero
        self.like = 0

    def like(self):
        self.like += 1

    def deslike(self):
        self.like -= 1

    @property
    def mensagem(self):
        return print("Lançamento no ano {}".format(self.ano))

    @property
    def likes(self):
        return self.like

class Filme(Programa):
    def __init__(self, ano, genero, duracao):
        super().__init__(ano, genero)
        self.duracao = duracao

cars = Filme(2006, "Animação", 117)

cars.like()

