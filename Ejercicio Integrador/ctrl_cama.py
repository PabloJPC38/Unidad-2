import numpy as np
from csv import reader
from mod_cama import Cama
from ctrl_medic import Ctrl_M

class Ctrl_C:

    def __init__(self,ruta:str,ruta2:str):

        self.__cama=np.array(Ctrl_C.Leer_Archivo(ruta))
        self.__medic=Ctrl_M(ruta2)

    def Obtener_Paciente(self,paciente)-> Cama | None:
        for x in self.__cama:
            if x.Get_NyA()==paciente:
                return x
        return None
    
    def Mostrar_Datos(self,paciente):
        x=self.Obtener_Paciente(paciente)
        if x is None:
            print("paciente no encontrado")
            return
        fecha=input("Ingrese fecha de alta con el formato .../.../...  :")
        x.Set_F_Alta(fecha)
        print()
        print(f"Paciente:{x.Get_NyA()}      Cama:{x.Get_Id()}       Habitación:{x.Get_Hab()}")
        print(f"Diagnóstico:{x.Get_Diag()}      Fecha de internación:{x.Get_F_Intern()}")
        print(f"Fecha de alta:{x.Get_F_Alta()}")
        print()
        self.__medic.Mostrar_Medicamentos(x.Get_Id())

    def Mostrar_X_Diagnostico(self,diag:str):
        for x in self.__cama:
            if ((x.Get_Diag()==diag) and (x.Get_Est()==True)):
                print(f"Paciente:{x.Get_NyA()}      Cama:{x.Get_Id()}       Habitación:{x.Get_Hab()}")
                print(f"Diagnóstico:{x.Get_Diag()}      Fecha de internación:{x.Get_F_Intern()}")

    @staticmethod
    def Leer_Archivo(ruta:str)->list[Cama]:
        with open(ruta,"r") as f:
            next(f)
            return list(map(lambda lista:Cama(int(lista[0]),int(lista[1]),bool(lista[2]),lista[3],lista[4],lista[5],lista[6]),reader(f,delimiter=";")))
    
    