from abc import ABCMeta, abstractmethod

#Classes abstratas
class Logistica(metaclass=ABCMeta):

    @abstractmethod
    def planeja_entrega(self):
        pass

    @abstractmethod
    def cria_transporte(self):
        pass

class Transporte(metaclass=ABCMeta):
    @abstractmethod
    def entrega(self):
        pass

# Classes concretas
class Caminhao(Transporte):
    def entrega(self):
        print("Efetuando entrega por Caminhão!")

class Barco(Transporte):
    def entrega(self):
        print("Efetuando entrega por barco!")

class Drone(Transporte):
    def entrega(self):
        print('Entregando encomendas pelo ar!')

class LogisticaTerrestre(Logistica):
    def planeja_entrega(self):
        print("Planejando logisticas por terra...")
    
    def cria_transporte(self):
        return Caminhao()

class LogisticaAerea(Logistica):
    def planeja_entrega(self):
        print("Planejando entregas pelo ar...")
    
    def cria_transporte(self):
        return Drone()

class LogisticaMaritima(Logistica):
    def planeja_entrega(self):
        print("Planejando entregas pela agua...")
    def cria_transporte(self):
        return Barco()