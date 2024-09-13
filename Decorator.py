from abc import ABCMeta, abstractmethod

class Component():
    @abstractmethod
    def operacao(self): pass


class Decorator(Component, metaclass=ABCMeta):
    
    def __init__(self, componente:Component):
        self.__componente = componente

    @property
    def componente(self):
        return self.__componente

    @abstractmethod
    def operacao(self):
        return self.__componente.operacao()


class ConcreteComponent(Component):

    def operacao(self):
        return("ComponenteConcreto")

class ConcreteDecoratorA(Decorator):

    def operacao(self):
        return f"--{self.componente.operacao()}--"

class ConcreteDecoratorB(Decorator):

    def operacao(self):
        return f"<{self.componente.operacao()}>"


if __name__ == "__main__":
    comp_simples = ConcreteComponent()
    print(f"Componente simples: {comp_simples.operacao()}")

    decorador_a = ConcreteDecoratorA(comp_simples)
    decorador_a2 = ConcreteDecoratorA(decorador_a)
    decorador_b = ConcreteDecoratorB(decorador_a2)
    decorador_b2 = ConcreteDecoratorB(decorador_b)

    print(f"Componente decorado: {decorador_b2.operacao()}")