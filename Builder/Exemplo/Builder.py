from abc import ABCMeta, abstractmethod, abstractproperty


class CozinhaFastFood(metaclass=ABCMeta):

    @abstractproperty
    def hamburguer(self): pass

    @abstractmethod
    def monta_hamburguer_pao_baixo(self): pass

    @abstractmethod
    def monta_hamburguer_alface(self): pass

    @abstractmethod
    def monta_hamburguer_tomate(self): pass

    @abstractmethod
    def monta_hamburguer_carne(self): pass

    @abstractmethod
    def monta_hamburguer_queijo(self): pass

    @abstractmethod
    def monta_hamburguer_cebola(self): pass

    @abstractmethod
    def monta_hamburguer_pao_cima(self): pass


class Hamburguer:

    def __init__(self):
        self._ingredientes = []

    def adiciona(self, ingrediente):
        self._ingredientes.append(ingrediente)

    def lista_ingredientes(self):
        print("Hamburguer:")
        for ingrediente in self._ingredientes:
            print(f"\t{ingrediente}")


class CozinhaHamburguer(CozinhaFastFood):

    def __init__(self):
        self.reset()

    def reset(self):
        self._hamburguer = Hamburguer()

    @property
    def hamburguer(self):
        hamburguer = self._hamburguer
        self.reset()
        return hamburguer

    def monta_hamburguer_pao_baixo(self):
        self._hamburguer.adiciona("Pão (parte de baixo)")

    def monta_hamburguer_alface(self):
        self._hamburguer.adiciona("Alface")

    def monta_hamburguer_tomate(self):
        self._hamburguer.adiciona("Tomate")

    def monta_hamburguer_carne(self):
        self._hamburguer.adiciona("Carne")

    def monta_hamburguer_queijo(self):
        self._hamburguer.adiciona("Queijo")

    def monta_hamburguer_cebola(self):
        self._hamburguer.adiciona("Cebola")

    def monta_hamburguer_pao_cima(self):
        self._hamburguer.adiciona("Pão (Parte de cima)")


class McDonalds:
    def __init__(self):
        self._cozinha = None

    @property
    def cozinha(self):
        return self._cozinha

    @cozinha.setter
    def cozinha(self, cozinha):
        self._cozinha = cozinha

    def hamburguer_simples(self):
        self.cozinha.monta_hamburguer_pao_baixo()
        self.cozinha.monta_hamburguer_carne()
        self.cozinha.monta_hamburguer_queijo()
        self.cozinha.monta_hamburguer_pao_cima()

    def hamburguer_duplo(self):
        self.cozinha.monta_hamburguer_pao_baixo()
        self.cozinha.monta_hamburguer_carne()
        self.cozinha.monta_hamburguer_queijo()
        self.cozinha.monta_hamburguer_carne()
        self.cozinha.monta_hamburguer_queijo()
        self.cozinha.monta_hamburguer_pao_cima()

    def hamburguer_completo(self):
        self.cozinha.monta_hamburguer_pao_baixo()
        self.cozinha.monta_hamburguer_alface()
        self.cozinha.monta_hamburguer_tomate()
        self.cozinha.monta_hamburguer_carne()
        self.cozinha.monta_hamburguer_queijo()
        self.cozinha.monta_hamburguer_cebola()
        self.cozinha.monta_hamburguer_pao_cima()


if __name__ == "__main__":
    mc = McDonalds()
    cozinha = CozinhaHamburguer()
    mc.cozinha = cozinha

    mc.hamburguer_simples()
    cozinha.hamburguer.lista_ingredientes()

    mc.hamburguer_duplo()
    cozinha.hamburguer.lista_ingredientes()

    mc.hamburguer_completo()
    cozinha.hamburguer.lista_ingredientes()
