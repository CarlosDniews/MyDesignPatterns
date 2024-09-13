class Diretor():
    def buildHtmlText(self, builder, mdLines):

        htmlBuilder = builder(mdLines)
        htmlBuilder.buildTitles()
        htmlBuilder.buildChars()
        htmlBuilder.buildLists()
        return htmlBuilder.getProduct()
        
