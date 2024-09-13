from abc import ABCMeta, abstractmethod

class Target(metaclass=ABCMeta):
    @abstractmethod
    def requisicao(self, valor):
        pass

class Adaptee:
    def requisicao_especifica(self, texto):
        print(f"<--{texto}-->")

class Adapter(Target):
    def __init__(self):
        super().__init__()
        self.__adaptador = Adaptee()
    
    def requisicao(self,valor):
        self.__adaptador.requisicao_especifica(valor)