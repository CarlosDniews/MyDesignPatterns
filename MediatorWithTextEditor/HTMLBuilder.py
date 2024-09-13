from abc import ABCMeta, abstractmethod, abstractproperty

class HTMLBuilder(metaclass=ABCMeta):

    @abstractproperty
    def buildTitles(self): pass

    @abstractproperty
    def buildChars(self): pass

    @abstractproperty
    def buildLists(self): pass

    @abstractproperty
    def getProduct(self): pass
