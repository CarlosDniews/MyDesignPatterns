from abc import ABCMeta, abstractmethod

class ContextoCafeteira():

    def __init__(self, estado):
        self._estado = None
        self.troca_estado(estado)
    
    def troca_estado(self, estado):
        print(f"Contexto: Trocando o estado para {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self 

    def requisicao1(self):
        self._estado.operacao1()
    
    def requisicao2(self):
        self._estado.operacao2()


class EstadoCafeteira(metaclass=ABCMeta):

    @property
    def contexto(self):
        return self._contexto
    
    @contexto.setter
    def contexto(self, contexto):
        self._contexto = contexto
    
    @abstractmethod
    def operacao1(self): pass

    @abstractmethod
    def operacao2(self): pass


class EstadoConcretoA(EstadoCafeteira):
    
    def operacao1(self):
        print("Estado Concreto A: lidando com a requisição 1")
        print("Estado Concreto A: Desejando mudar o estado do contexto")
        self.contexto.troca_estado(EstadoConcretoB())

    def operacao2(self):
        print("Estado Concreto A: Lidando com a requisição 2")
    

class EstadoConcretoB(EstadoCafeteira):

    def operacao1(self):
        print("Estado Concreto B: Lidando com a requisição 1")
    
    def operacao2(self):
        print("Estado Concreto B: Lidando com a operação 2")
        print("Estado Concreto B: Desejando mudar o estado do contexto")

        self.contexto.troca_estado(EstadoConcretoA())

if __name__ == "__main__":
    
    cafeteira = ContextoCafeteira(EstadoConcretoA())
    cafeteira.requisicao1()
    cafeteira.requisicao2()