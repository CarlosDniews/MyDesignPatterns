import sys


class Singleton(type):

    def __init__(cls, object_or_name, bases, dict):
      super().__init__(object_or_name, bases, dict)
      cls._instancia = None
    
    def __call__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__call__(*args, **kwargs)
        return cls._instancia


class ConexaoDB(metaclass=Singleton):

    def __init__(self):
        self._conectado = False
        self._endereco = None

    def conectar(self, endereco):
        self._endereco = endereco
        print(f"conectando ao endereço {self._endereco}")
        self._conectado = True
    
    def executa_query(self, query):
        if self._conectado is True:
            print(f"Executando consulta {query}")
        else:
            raise Exception("Banco não conectado")
    
    def esta_conectado(self):
        return self._conectado


db1 = ConexaoDB()
db1.conectar("127.0.0.1")
print(db1.esta_conectado())
db1.executa_query("SELECT * FROM TABELA")

db2 = ConexaoDB()
print(db2.esta_conectado())
db2.executa_query("SELECT * FROM OUTRA_TABELA")


### classes estendidas
class MySQL(ConexaoDB):
    
    def __init__(self):
        super().__init__()
        self.nome_banco = "mysql"

class MongoDB(ConexaoDB):
    def __init__(self):
        super().__init__()
        self.nome_banco = "MongoDB"

db3 = MySQL()
db4 = MongoDB()
db5 = MongoDB()
print(db3)
print(db4)
print(db5)
print(db3.esta_conectado())
print(db4.esta_conectado())
