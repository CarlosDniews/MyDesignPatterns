from FactoryMethod import LogisticaMaritima, LogisticaTerrestre, Logistica, LogisticaAerea

class EmpresaDeTransporte:
    def __init__(self):
        self._logisticas = list()
    
    def add_logistica(self,setor:Logistica):
        if isinstance(setor,Logistica):
            self._logisticas.append(setor)
        else:
            raise TypeError("Setor deve ser uma implementalção de Logistica!")
    
    def planejamento(self):
        for logistica in self._logisticas:
            logistica.planeja_entrega()

    def realiza_entregas(self):
        for logistica in self._logisticas:
            transporte = logistica.cria_transporte() # Aqui é chamado o FactoryMethod 
            transporte.entrega()


if __name__ == "__main__":
    print("Criando empresa de transporte: Planet Express")
    print('''
    
                         `. ___
                        __,' __`.                _..----....____
            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
    ,'________________                          \\`-._`-','
     `._              ```````````------...___   '-.._'-:
        ```--.._      ,.                     ````--...__\\-.
                `.--. `-`                       ____    |  |`
                  `. `.                       ,'`````.  ;  ;`
                    `._`.        __________   `.      \\'__/`
                       `-:._____/______/___/____`.     \\  `
                                   |       `._    `.    \\
                                   `._________`-.   `.   `.___
                                                 SSt  `------'`
    ''')
    planet_express = EmpresaDeTransporte()
    planet_express.add_logistica( LogisticaTerrestre())
    planet_express.add_logistica( LogisticaMaritima() )
    planet_express.add_logistica( LogisticaAerea() )
    planet_express.planejamento()
    planet_express.realiza_entregas()