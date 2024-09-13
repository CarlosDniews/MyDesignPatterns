from abc import ABCMeta, abstractmethod

#Subject
class Servidor(metaclass=ABCMeta):

    @abstractmethod
    def requisicao(self,endereco,conteudo,autenticacao=None):
        pass

#RealSubject
class ServidorHTTP(Servidor):

    def requisicao(self, endereco, conteudo, autenticacao=None):
        return f"Retornando dados de {endereco}, para conteudo {conteudo}, autenticado:{autenticacao}"

# Proxy
class Proxy(Servidor):

    def __init__(self):      
        self.__servidor = ServidorHTTP()
        self._dominios_bloquados = ["jogos.com","facebook.com"]
        self._dominios_autenticados = ["ieee.org","unisinos.br"]
    
    def requisicao(self,endereco,conteudo,autenticacao=None):
        if endereco in self._dominios_bloquados:
            return f"Não é possível acessar {endereco} nesta rede"
        if endereco in self._dominios_autenticados:
            return self.__servidor.requisicao(endereco,conteudo,autenticacao="Autenticado pelo proxy!")
        return self.__servidor.requisicao(endereco,conteudo)


if __name__ == "__main__":
    proxy = Proxy()
    
    r1 = proxy.requisicao("jogos.com","teste")
    print(r1)

    r2 = proxy.requisicao("unisinos.br","teste")
    print(r2)

    r3 = proxy.requisicao("google.com","teste")
    print(r3)