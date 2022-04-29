
class Viajero_Frecuente:
    def __init__(self,num,DNI,nbre,ape,millas):
        self.__num=num
        self.__DNI=DNI
        self.__nbre=nbre
        self.__ape=ape
        self.__millas=millas
    
    def numero_viajero(self):
        return self.__num
    def cantidadTotaldeMillas(self):
        return self.__millas
    def acumularMillas(self,cant):
        self.__millas+=cant
        return self.__millas
    def canjearMillas(self,cant_canj):
        if cant_canj <= self.__millas:
            self.__millas-=cant_canj
            return self.__millas
        else:
            print("Error en la operación")