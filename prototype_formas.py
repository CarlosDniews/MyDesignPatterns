from abc import ABCMeta, abstractmethod

"""
Implementação "manual", sem o uso da biblioteca copy
"""

class Forma:

    def __init__(self,referencia=None):
        if referencia is None:
            self.x = None
            self.y = None
            self.cor = None
        else:
            self.x = referencia.x
            self.y = referencia.y
            self.cor = referencia.cor
    
    @abstractmethod
    def clonar(self): pass

class Retangulo(Forma):

    def __init__(self, referencia=None):
        super().__init__(referencia=referencia)
        if referencia is None:
            self.largura = None
            self.altura = None
        else:
            self.largura = referencia.largura
            self.altura = referencia.altura
    
    def clonar(self):
        return Retangulo(self) # Passa o prórpio objeto como referência

    def __repr__(self):
        return f"<Retangulo x:{self.x}, y:{self.y}, cor:{self.cor}, largura:{self.largura}, altura:{self.altura} @{hex(id(self))}>"

class Circulo(Forma):

    def __init__(self, referencia=None):
        super().__init__(referencia=referencia)
        if referencia is None:
            self.raio = None
        else:
            self.raio = referencia.raio
    
    def clonar(self):
        return Circulo(self)
    
    def __repr__(self):
        return f"<Circulo x:{self.x}, y:{self.y}, cor:{self.cor}, raio: {self.raio} @{hex(id(self))}>"

if __name__ == "__main__":
        lista_de_formas = list()

        circulo = Circulo()
        circulo.x = 10
        circulo.y = 10
        circulo.raio = 20
        circulo.cor = "Verde"
        lista_de_formas.append(circulo)

        outro_circulo = circulo.clonar()
        outro_circulo.cor = "Amarelo"
        lista_de_formas.append(outro_circulo)

        retangulo = Retangulo()
        retangulo.x = 5
        retangulo.y = 20
        retangulo.largura = 10
        retangulo.altura = 20
        retangulo.cor = "Vermelho"
        lista_de_formas.append(retangulo)

        copia_lista = []

        for item in lista_de_formas:
            copia_lista.append(item.clonar())
        
        print(lista_de_formas)
        print(copia_lista)