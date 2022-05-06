from os import path
from csv import reader
from mod_medic import medicamento

class Ctrl_M:

    def __init__(self,ruta:str):

        self.__medic=list(Ctrl_M.Leer_Archivo(ruta))
    
    def  Mostrar_Medicamentos(self,ID:int):
        total=0
        print("Medicamento/monodroga        Presentación        Cantidad        Precio")
        print()
        for x in self.__medic:
            if x.Get_Id_cama()==ID:
                print(f"{x.Get_Nbre()}/{x.Get_md()}        {x.Get_PPT()}            {x.Get_Cant()}              {x.Get_Precio()}")
                total+=x.Get_Cant()*x.Get_Precio()
        print()
        print("Total adeudado:",total)

    @staticmethod
    def Leer_Archivo(path: str) -> list[medicamento]:
        with open(path, "r") as f:
            next(f)
            return list(map(lambda lista: medicamento(int(lista[0]),int(lista[1]),lista[2],lista[3],lista[4],int(lista[5]),float(lista[6])),reader(f,delimiter=";")))


