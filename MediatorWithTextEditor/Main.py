from MDtoHTMLBuilder import MDtoHTMLBuilder
from Diretor import Diretor
from FileManager import FileManager

htmlFileManager = FileManager("./arquivoHTML.html", "w+")
mdFileManager = FileManager("./arquivoMD.md", "r")

diretor = Diretor()
produto =  diretor.buildHtmlText(MDtoHTMLBuilder, mdFileManager.getLinesFromFile())
htmlFileManager.write(produto)

print("Executado com sucesso!")