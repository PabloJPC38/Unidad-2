class Registro:
    def __init__(self,temp,humed,pat):
        self.__temp=temp
        self.__humed=humed
        self.__pat=pat
    def Temp(self):
        return float(self.__temp)
    def Humed(self):
        return float(self.__humed)
    def Press(self):
        return float(self.__pat)