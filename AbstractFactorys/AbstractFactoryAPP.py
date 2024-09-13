import pyglet
from abc import ABCMeta, abstractmethod
from PySide2.QtWidgets import QApplication, QLabel


class LabelAbstrata(metaclass=ABCMeta):
    
    @abstractmethod
    def nova(self, texto): pass

    @abstractmethod
    def render(self): pass

class AppAbstrata(metaclass=ABCMeta):

    @abstractmethod
    def nova_app(self): pass

    @abstractmethod
    def executar(self): pass

    @abstractmethod
    def adiciona_label(self, texto) -> LabelAbstrata: pass




### Classes concretas

class PygletLabel(LabelAbstrata):
    def nova(self, texto):
        self.label = pyglet.text.Label(texto,
                          font_name='Times New Roman',
                          font_size=36,
                          x=200, y=200,
                          anchor_x='center', anchor_y='center')
    def render(self):
        self.label.draw()


class PygletAPP(AppAbstrata):

    def __init__(self):
        self.app = None
        self.janela = None
    
    def nova_app(self):
        self.janela = pyglet.window.Window()
        janela = self.janela
        self.janela.clear()
        @janela.event
        def on_draw():
            self.janela.clear()
            self.label.render()
    
    def executar(self):
        pyglet.app.run()
    
    def adiciona_label(self,texto):
        self.label = PygletLabel()
        self.label.nova(texto)

class QTLabel(LabelAbstrata):
    def nova(self, texto):
        self.label = QLabel(texto)
    
    def render(self):
        self.label.show()

class QTApp(AppAbstrata):
    def __init__(self):
        self.app = None
        self.label = None
    
    def nova_app(self):
        self.app = QApplication()
    
    def executar(self):
        self.app.exec_()
    
    def adiciona_label(self, texto):
        self.label = QTLabel()
        self.label.nova(texto)
        self.label.render()



