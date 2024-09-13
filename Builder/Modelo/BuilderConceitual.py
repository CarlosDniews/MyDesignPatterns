from abc import ABCMeta, abstractmethod, abstractproperty

class Construtor(metaclass=ABCMeta):

    @abstractproperty
    def produto(self):
        pass

    @abstractmethod
    def produz_parte_a(self):
        pass

    @abstractmethod
    def produz_parte_b(self):
        pass

    @abstractmethod
    def produz_parte_c(self):
        pass


class Produto1:
    def __init__(self):
        self.partes = []

    def adiciona(self, parte):
        self.partes.append(parte)

    def lista_partes(self):
        print(f"Partes do produto: {', '.join(self.partes)}")


class ConstrutorConcreto1(Construtor):

    def __init__(self):
        self.reset()

    def reset(self):
        self._produto = Produto1()

    @property
    def produto(self):
        produto = self._produto
        self.reset()
        return produto

    def produz_parte_a(self):
        self._produto.adiciona("Parte A")

    def produz_parte_b(self):
        self._produto.adiciona("Parte B")

    def produz_parte_c(self):
        self._produto.adiciona("Parte C")


class Diretor:
    def __init__(self):
        self._construtor = None

    @property
    def construtor(self):
        return self._construtor

    @construtor.setter
    def construtor(self, construtor):
        self._construtor = construtor

    def constroi_produto_minimo(self):
        self.construtor.produz_parte_a()

    def constroi_produto_completo(self):
        self.construtor.produz_parte_a()
        self.construtor.produz_parte_b()
        self.construtor.produz_parte_c()