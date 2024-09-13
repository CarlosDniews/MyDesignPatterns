from HTMLBuilder import HTMLBuilder
from Texto import Texto

class MDtoHTMLBuilder(HTMLBuilder):
    def __init__(self, lista_md):
        self.reset()
        self.lista_md = lista_md

    def reset(self):
        self._textosHTMLs = Texto()

    def buildTitles(self):
        for linha in self.lista_md:
            if linha.count("#") != 0:
                counter = linha.count("#")
                contador = str(counter)
                texto_formatado = linha.replace("\n","")
                texto_formatado = texto_formatado.replace("#","")
                self._textosHTMLs.adiciona("<h"+ contador + "> " + texto_formatado + "</h" + contador + ">\n")

    def buildChars(self):
        for linha in self.lista_md:
            if linha.count("*") == 2:
                texto_formatado = linha.replace("\n","")
                texto_formatado = texto_formatado.replace("*","")
                self._textosHTMLs.adiciona("<em>" + texto_formatado + "</em> \n")

            elif linha.count("*") == 4:
                texto_formatado = linha.replace("\n","")
                texto_formatado = texto_formatado.replace("*","")
                self._textosHTMLs.adiciona("<strong>" + texto_formatado + "</strong> \n")

            elif linha.count("*") == 6:
                texto_formatado = linha.replace("\n","")
                texto_formatado = texto_formatado.replace("*","")
                self._textosHTMLs.adiciona("<strong><em>" + texto_formatado + "</em></strong> \n")

    def buildLists(self):
        if not any("- " in linha for linha in self.lista_md):
            return
        self._textosHTMLs.adiciona("<ul>\n")
        for linha in self.lista_md:
            if linha.count("- ") == 1:
                texto_formatado = linha.replace("\n","")
                texto_formatado = texto_formatado.replace("-","")
                self._textosHTMLs.adiciona("<li>" + texto_formatado + "</li>\n")
        self._textosHTMLs.adiciona("</ul>\n")

    def getProduct(self):
        return self._textosHTMLs.convertLinestoString()