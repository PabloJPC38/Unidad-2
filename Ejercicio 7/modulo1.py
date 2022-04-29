
from __future__ import annotations

class Viajero_Frecuente:
    def __init__(self,num,DNI,nbre,ape,millas):
        self.__num=num
        self.__DNI=DNI
        self.__nbre=nbre
        self.__ape=ape
        self.__millas=millas

    def Get_Num(self):
        return int(self.__num)

    def Get_Millas(self):
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

    def __gt__(self,otro):

        return self.__millas>otro.__millas

    def __eq__(self,otro):
        
        if type(otro)==int:

            return self.__num==otro
        else:
            return self.__millas==otro

    def __ge__(self,otro):

        return self.__millas>=otro

    def __add__(self,otro) -> Viajero_Frecuente:

        self.acumularMillas(otro)
        return self

    def __sub__(self,otro) -> Viajero_Frecuente:

        self.canjearMillas(otro)
        return self

    def __radd__(self,otro) -> Viajero_Frecuente:

        self.acumularMillas(otro)
        return self

    def __rsub__(self,otro) -> Viajero_Frecuente:

        self.canjearMillas(otro)
        return self
