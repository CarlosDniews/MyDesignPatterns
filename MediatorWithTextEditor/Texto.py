class Texto:
    def __init__(self):
        self._linhas = []

    def adiciona(self, linha):
        self._linhas.append(linha)

    def get_linhas(self):
        return self._linhas

    def convertLinestoString(self):
        text = ""
        for linha in self._linhas:
            text += linha
        return text