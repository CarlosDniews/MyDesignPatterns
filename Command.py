# Implementação adaptada de https://refactoring.guru/pt-br/design-patterns/command/python/example

from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


class CommandSimples(Command):

    def __init__(self, payload):
        self.payload = payload
    
    def executar(self):
        print("CommandSimples: Eu consigo fazer coisas simples como imprimir na tela:")
        print(self.payload)

class CommandComplexo(Command):

    def __init__(self, receiver, a, b):
        self.receiver = receiver
        self._a = a
        self._b = b
    
    def executar(self):
        print("CommandComplexo: Coisas complexas devem ser feitas pelo objeto Receiver")
        self.receiver.faz_algo(self._a)
        self.receiver.faz_outra_coisa(self._b)
    
class Receiver:

    def faz_algo(self,a):
        print(f"\nReceiver: Trabalhando em {a}",end="")
    
    def faz_outra_coisa(self,b):
        print(f"\nReceiver: Também trabalhando em {b}")

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command
    
    def set_on_finish(self, command):
        self._on_finish = command
    
    def faz_algo_importante(self):
        print("Invoker: Alguem deseja algo pronto antes que eu inicie?")
        if isinstance(self._on_start, Command):
            self._on_start.executar()
        
        print("Invoker: ... Fazendo algo muito importante....")

        print("Invoker: Alguem quer fazer algo depois que eu termine?")
        if isinstance(self._on_finish, Command):
            self._on_finish.executar()

if __name__ == "__main__":
    
    invocador = Invoker()
    invocador.set_on_start(CommandSimples("Diga olá!"))
    destinatario = Receiver()
    invocador.set_on_finish(CommandComplexo(destinatario,"Enviar email","Salvar relatório"))
    invocador.faz_algo_importante()