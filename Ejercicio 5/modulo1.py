from operator import countOf
from pydoc import ModuleScanner


class PlanAhorro:

    __plan_cuota=12
    __cuotas_licitar=5

    def __init__(self,cod,mod,vers,valor):
        self.__cod=cod
        self.__mod=mod
        self.__vers=vers
        self.__valor=valor
    
    def Mostrar(self):
        print(self.__cod," ",self.__mod," ",self.__vers)
    
    def Actualizar(self,v):
        self.__valor=v
    
    def Mostrar_Valores_Actualizados(self):
        print(self.__cod," ",self.__mod," ",self.__vers," ",self.__valor)
    
    def Valor_Cuota(self):
        return ((self.__valor/self.__plan_cuota)+(self.__valor*0.1))
    
    def Get_Modelo(self):
        return self.__mod
    
    def Get_Valor(self):
        return self.__valor
    
    @classmethod

    def Cantidad_De_Cuotas(cls):
        return cls.__cuotas_licitar
    
    @classmethod
    def Modificar_Cantidad_Cuotas(cls,c):
        cls.__cuotas_licitar=c
    
    @classmethod
    def Get_Cuotas_Licitar(cls):
        return cls.__cuotas_licitar
    




