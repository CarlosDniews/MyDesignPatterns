from abc import ABCMeta, abstractmethod

class Forma(metaclass=ABCMeta):
    def __init__(self):
        self.cor:Cor = None

    @abstractmethod
    def nome_forma(self): pass

    def __repr__(self):
        return f"<Forma: {self.nome_forma()} {self.cor.get_color()}>"

class Cor(metaclass=ABCMeta):
    @abstractmethod
    def get_color(self): pass

class Vermelho(Cor):
    def __init__(self):
        self._cor = "vermelho"
    def get_color(self):
        return self._cor

class Azul(Cor):
    def __init__(self):
        self._cor = "azul"
    def get_color(self):
        return self._cor

class Circulo(Forma):
    def __init__(self):
        self._formato = "circulo"

    def nome_forma(self):
        return self._formato

class Triangulo(Forma):
    def __init__(self):
        self._formato = "Triangulo"
    def nome_forma(self):
        return self._formato

class Retangulo(Forma):
    def __init__(self):
        self._formato = "retângulo"

    def nome_forma(self):
        return self._formato


if __name__ == "__main__":
    c1 = Circulo()
    c2 = Circulo()
    r1 = Retangulo()
    r2 = Retangulo()
    t1 = Triangulo()

    c1.cor = Vermelho()
    c2.cor = Azul()
    r1.cor = Vermelho()
    r2.cor = Azul()
    t1.cor = Vermelho()

    print(c1)
    print(c2)
    print(r1)
    print(r2)
    print(t1)

