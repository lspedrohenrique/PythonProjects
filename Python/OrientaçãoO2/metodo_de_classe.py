class Funcionario:
    prefixo = 'Instrutor'

    @classmethod #I have access to class attributes through a class method, and I can access the class method through a class
    def info(cls):
        return f'Esse é um {cls.prefixo}'


class FolhaDePagamento:
    @staticmethod #No reference to the class itself
    def log():
        return f'Isso é um log qualquer'