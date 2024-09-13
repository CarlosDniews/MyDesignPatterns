from abc import ABCMeta, abstractmethod

# interfaces

class FabricaAbstrata(metaclass=ABCMeta):

    @abstractmethod
    def cria_produto_a(self): pass

    @abstractmethod
    def cria_produto_b(self): pass



class ProdutoAbstratoA(metaclass=ABCMeta):

    def tipo(self):
        return "A"
    
    @abstractmethod
    def modelo(self): pass

    def identificacao(self):
        return f"{self.tipo()}-{self.modelo()}"

class ProdutoAbstratoB(metaclass=ABCMeta):

    def tipo(self):
        return "B"
    
    @abstractmethod
    def modelo(self): pass

    def identificacao(self):
        return f"{self.tipo()}-{self.modelo()}"

#classes concretas

class ProdutoConcretoA1(ProdutoAbstratoA):

    def modelo(self):
        return "1"

class ProdutoConcretoA2(ProdutoAbstratoA):

    def modelo(self):
        return "2"

class ProdutoConcretoB1(ProdutoAbstratoB):

    def modelo(self):
        return "1"

class ProdutoConcretoB2(ProdutoAbstratoB):

    def modelo(self):
        return "2"

class FabricaConcreta1(FabricaAbstrata):
    
    def cria_produto_a(self):
        return ProdutoConcretoA1()
    
    def cria_produto_b(self):
        return ProdutoConcretoB1()

class FabricaConcreta2(FabricaAbstrata):

    def cria_produto_a(self):
        return ProdutoConcretoA2()

    def cria_produto_b(self):
        return ProdutoConcretoB2()
