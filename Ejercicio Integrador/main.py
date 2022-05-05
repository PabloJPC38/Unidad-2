from os import path
from ctrl_cama import Ctrl_C

if __name__=="__main__":
    obj=Ctrl_C(path.dirname(__file__)+"/camas.csv",path.dirname(__file__)+"/medicamentos.csv")
    print()
    obj.Mostrar_Datos(input("Ingrese Nombre y Apellido:"))
    print()
    obj.Mostrar_X_Diagnostico(input("Ingrese diagnóstico:"))
