from csv import reader
from os import path
import numpy as np



class Cama:

    def __init__(self,id:int,hab,estado:bool,diag,f_intern,f_alta=None,NyA=None,):

        self.__id=id
        self.__hab=hab
        self.__estado=estado
        self.__NyA=NyA
        self.__diag=diag
        self.__f_intern=f_intern
        self.__f_alta=f_alta

class Ctrl_Cama(Cama):

    def Leer_Archivo(self):

        with open(path.dirname(__file__)+ "/camas.csv","r") as f:
            next(f)
            return list(map(lambda lista: (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6]),reader(f,delimiter=";")))

