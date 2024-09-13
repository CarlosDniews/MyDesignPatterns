from abc import ABCMeta, abstractmethod

class Equipament(metaclass=ABCMeta):
    def __init__(self):
        self._volume = None
        self._canal = None
        self._modelo = None
        self._estado = None

    @abstractmethod
    def getModel(self): pass

    @abstractmethod
    def isEnable(self): pass

    @abstractmethod
    def enable(self): pass

    @abstractmethod
    def disable(self): pass

    @abstractmethod
    def getVolume(self): pass

    @abstractmethod
    def setVolume(self): pass

    @abstractmethod
    def getChannel(self): pass

    @abstractmethod
    def setChannel(self): pass


class Control(metaclass=ABCMeta):
    def __init__(self):
        self.equipamento:Equipament = None
        self.modelo = None

    def __repr__(self):
        return f"<Modelo: { self.equipamento.getModel()} \n Volume: {self.equipamento.getVolume()} \n Canal: {self.equipamento.getChannel()} \n está {self.equipamento._estado}\n>"

    @abstractmethod
    def togglePower(self): pass

    @abstractmethod
    def volumeUp(self): pass

    @abstractmethod
    def volumeDown(self): pass

    @abstractmethod
    def channelUp(self): pass

    @abstractmethod
    def channelDown(self): pass


class Radio(Equipament):
    def __init__(self):
        self._volume = 0
        self._canal = 1
        self._modelo = "Radio"
        self._estado = "desligado"
    
    def getModel(self):
        return self._modelo

    def isEnable(self): 
        if (self._estado == "desligado"):
            self._estado = "ligado"

        else:
            self._estado = "desligado"
  
    def enable(self):
        self._estado = "ligado"
    
    def disable(self):
        self._estado = "desligado"
    
    def getVolume(self):
        return self._volume
    
    def setVolume(self, vol):
        self._volume = vol

    def getChannel(self):
        return self._canal
    
    def setChannel(self, can):
        self._canal = can


class TV(Equipament):
    def __init__(self):
        self._volume = 1
        self._canal = 1
        self._modelo = "TV"
        self._estado = "desligado"
    
    def getModel(self):
        return self._modelo

    def isEnable(self): 
        if (self._estado == "desligado"):
            self._estado = "ligado"

        else:
            self._estado = "desligado"
  
    def enable(self):
        self._estado = "ligado"
    
    def disable(self):
        self._estado = "desligado"
    
    def getVolume(self):
        return self._volume
    
    def setVolume(self, vol):
        self._volume = vol

    def getChannel(self):
        return self._canal
    
    def setChannel(self, can):
        self._canal = can


class ControleConcreto(Control):
    def togglePower(self):
        self.equipamento.isEnable()

    def volumeUp(self):
        old = self.equipamento.getVolume()
        self.equipamento.setVolume(old + 1)

    def volumeDown(self):
        old = self.equipamento.getVolume()
        if(old == 0):
            self.equipamento.getVolume()
        else:
            self.equipamento.setVolume(old - 1)
    
    def channelUp(self):
        old = self.equipamento.getChannel()
        self.equipamento.setChannel(old + 1)
    
    def channelDown(self):
        old = self.equipamento.getChannel()
        if(old == 0):
            self.equipamento.getChannel()
        else:
            self.equipamento.setChannel(old - 1)

controle1 = ControleConcreto()
controle2 = ControleConcreto()

controle1.equipamento = TV()
controle2.equipamento = Radio()

print(controle1)
print(controle2)
    
controle1.togglePower()
controle1.volumeUp()
controle1.channelUp()

controle2.togglePower()
controle2.volumeDown()
controle2.channelDown()

print(controle1)
print(controle2)