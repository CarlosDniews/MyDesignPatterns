# código baseado no exemplo disponível em: https://refactoring.guru/design-patterns/factory-method
from abc import ABCMeta, abstractmethod

# Classes abstratas
class Product(metaclass=ABCMeta):
    # Classe abstrata de Produto
    @abstractmethod
    def operation(self):
        pass

class Creator(metaclass=ABCMeta):

    #Classe abstrata de Criador
    @abstractmethod
    def create_product(self):
        # Este é o nosso método fábrica, que deve ser implementado pelas subclasses
        pass
    
    def some_operation(self):
        produto = self.create_product()
        return f"Criador: O mesmo código do criador funcionando com {produto.operation()}"

# Implementações
class ConcreteProduct1(Product):
    def operation(self):
        return "{Resultado do ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self):
        return "{Resultado do ConcreteProduct2}"

class ConcreteCreator1(Creator):
    def create_product(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def create_product(self):
        return ConcreteProduct2()

# aplicação

def client_code(criador:Creator):
    print(f"Cliente: Eu não conheço a classe criadora, mas continuo funcionando.\n{criador.some_operation()}")

if __name__ == "__main__":
    print("App: Chamando o criador 1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Chamando o criador 2")
    client_code(ConcreteCreator2())